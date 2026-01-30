import * as THREE from "https://cdn.skypack.dev/three";

export class Zone {
  constructor(scene) {
    this.radius = 80;

    this.mesh = new THREE.Mesh(
      new THREE.CircleGeometry(this.radius, 64),
      new THREE.MeshBasicMaterial({ color: 0x00ffff, wireframe: true })
    );
    this.mesh.rotation.x = -Math.PI / 2;
    scene.add(this.mesh);
  }

  update() {
    if (this.radius > 10) {
      this.radius -= 0.01;
      this.mesh.geometry.dispose();
      this.mesh.geometry = new THREE.CircleGeometry(this.radius, 64);
    }
  }

  isInside(pos) {
    return pos.length() < this.radius;
  }
}
