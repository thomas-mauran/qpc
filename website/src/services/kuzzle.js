import { Kuzzle, WebSocket } from 'kuzzle-sdk';

export default new Kuzzle(new WebSocket(window.location.hostname));
