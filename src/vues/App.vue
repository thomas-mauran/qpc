<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import { onMounted, ref } from 'vue';
import kuzzle from '../services/kuzzle';

let inputAnswer = ref('');

let question = ref('');
let answer = ref('');
let answerTab = ref(null);

let answerIsTrue = ref(null);

async function retrieveData() {
    console.log('retrieving data');
    await kuzzle.connect();
    let numberOfQuestions = await kuzzle.document.count('qpc', 'questions');
    let randomInt = Math.floor(Math.random() * (numberOfQuestions - 1));
    let questionQuery = await kuzzle.document.search('qpc', 'questions', {
        query: {
            match: {
                id: randomInt,
            },
        },
    });

    question.value = questionQuery.hits[0]._source.question;
    answer.value = questionQuery.hits[0]._source.answer;
    answerTab.value = answer.value.split('/');
}

// Fonction pour comparer l'input et la liste de réponses

function checkAnswer() {
    // On enlève les maj et les espaces
    let convertedString = inputAnswer.value.toLocaleLowerCase();
    convertedString = convertedString.replaceAll(' ', '');

    answerTab.value.forEach((a) => {
        // On enlève les maj et les espaces + on remplace les appostrophes

        let tempA = a.toLocaleLowerCase();
        tempA = tempA.replaceAll(' ', '');
        tempA = tempA.replaceAll('’', "'");

        // Si les 2 valeures sont égales answerIsTrue devient true
        if (tempA == convertedString) {
            answerIsTrue.value = true;
            console.log('singe');
            return;
        }
    });
    // answerIsTrue est toujours nulle la réponse est donc fausse
    if (answerIsTrue.value == null) answerIsTrue.value = false;

    return;
}

// Au load de la page on recup les datas
onMounted(() => {
    retrieveData();
});

function nextQuestion() {
    question.value = '';
    answer.value = '';
    answerIsTrue.value = null;
    inputAnswer.value = '';

    retrieveData();
}

document.addEventListener('keydown', (key) => {
    // if(answerIsTrue.value == null){
    //     checkAnswer()
    // }
    if (key.code == 'Enter') {
        answerIsTrue.value == null ? checkAnswer() : nextQuestion();
    }
});
</script>

<template>
    <div>
        <h1>{{ question }}</h1>
        <h2 v-if="answerIsTrue" class="rightAnswer">Correct answer</h2>
        <h2 v-if="answerIsTrue == false" class="wrongAnswer">Wrong answer</h2>

        <div v-if="answerIsTrue != null">
            <h2>Answer : {{ answer }}</h2>
            <button @click="nextQuestion">Next question</button>
        </div>
        <div v-if="answerIsTrue == null">
            <input
                class="input"
                placeholder="Ta réponse"
                type="text"
                v-model="inputAnswer"
            />
            <button @click="checkAnswer">Check</button>
        </div>
    </div>
</template>

<style scoped>
.input {
    font-size: 2em;
}

.rightAnswer {
    color: green;
}
.wrongAnswer {
    color: red;
}
</style>
