import * as THREE from "https://cdn.skypack.dev/three";

export class Player {
  constructor(scene) {
    this.health = 100;
    this.mesh = new THREE.Mesh(
      new THREE.BoxGeometry(1, 2, 1),
      new THREE.MeshStandardMaterial({ color: 0x0000ff })
    );
    this.mesh.position.set(0, 10, 0);
    scene.add(this.mesh);
  }

  update(zone) {
    // Gravity
    if (this.mesh.position.y > 1) this.mesh.position.y -= 0.1;

    // Zone damage
    if (!zone.isInside(this.mesh.position)) {
      this.health -= 0.05;
      document.getElementById("health").innerText =
        `Health: ${Math.max(0, this.health.toFixed(0))}`;
    }
  }
}
