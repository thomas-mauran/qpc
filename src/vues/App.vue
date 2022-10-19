<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import { onMounted, ref } from 'vue';
import kuzzle from '../services/kuzzle';

let inputAnswer = ref('');

let question = ref('');
let answer = ref('');

async function retrieveData() {
    console.log('retrieving data');
    await kuzzle.connect();
    let numberOfQuestions = await kuzzle.document.count('qpc', 'questions');
    let randomInt = Math.floor(Math.random() * (numberOfQuestions - 1));
    console.log(randomInt);
    let questionQuery = await kuzzle.document.search('qpc', 'questions', {
        query: {
            match: {
                id: randomInt,
            },
        },
    });

    question.value = questionQuery.hits[0]._source.question;
    answer.value = questionQuery.hits[0]._source.answer;
}

function checkAnswer() {
    return;
}

onMounted(() => {
    retrieveData();
});
</script>

<template>
    <div>
        <h1>{{ question }}</h1>
        <input
            class="input"
            placeholder="Ta réponse"
            type="text"
            v-model="inputAnswer"
        />
        <button @click="checkAnswer">Check</button>
    </div>
</template>

<style scoped>
.input {
    font-size: 2em;
}
</style>
