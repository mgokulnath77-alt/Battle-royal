import * as THREE from "https://cdn.skypack.dev/three";

export class Bot {
  constructor(scene) {
    this.alive = true;
    this.health = 100;

    this.mesh = new THREE.Mesh(
      new THREE.BoxGeometry(1, 2, 1),
      new THREE.MeshStandardMaterial({ color: 0xff0000 })
    );
    this.mesh.position.set(
      Math.random() * 80 - 40,
      10,
      Math.random() * 80 - 40
    );
    scene.add(this.mesh);
  }

  update(player, zone) {
    if (!this.alive) return;

    // Move toward player
    this.mesh.position.lerp(player.mesh.position, 0.002);

    // Zone damage
    if (!zone.isInside(this.mesh.position)) {
      this.health -= 0.1;
    }

    if (this.health <= 0) {
      this.alive = false;
      this.mesh.visible = false;
    }
  }
}
