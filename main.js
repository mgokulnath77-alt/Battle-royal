import * as THREE from "https://cdn.skypack.dev/three";
import { Player } from "./player.js";
import { Bot } from "./bot.js";
import { Zone } from "./zone.js";

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x87ceeb);

const camera = new THREE.PerspectiveCamera(
  75, window.innerWidth / window.innerHeight, 0.1, 1000
);
camera.position.set(0, 20, 20);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Ground
const ground = new THREE.Mesh(
  new THREE.PlaneGeometry(200, 200),
  new THREE.MeshStandardMaterial({ color: 0x228b22 })
);
ground.rotation.x = -Math.PI / 2;
scene.add(ground);

// Light
scene.add(new THREE.HemisphereLight(0xffffff, 0x444444, 1));

// Player
const player = new Player(scene);

// Bots
const bots = [];
for (let i = 0; i < 19; i++) {
  bots.push(new Bot(scene));
}

// Zone
const zone = new Zone(scene);

function animate() {
  requestAnimationFrame(animate);

  player.update(zone);
  bots.forEach(bot => bot.update(player, zone));
  zone.update();

  document.getElementById("players").innerText =
    `Players Left: ${1 + bots.filter(b => b.alive).length}`;

  renderer.render(scene, camera);
}
animate();
