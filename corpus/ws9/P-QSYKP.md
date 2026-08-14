---
schema: qual/card@1
id: P-QSYKP
kind: problem
title: Let $v$ be a trigonometric polynomial in two variables, i.e.
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - pdes
  - norms
relations: []
review: draft
---

:::{.problem title="?"}
Let $v$ be a trigonometric polynomial in two variables, i.e.
$$v(x,y) = \sum_{n,m\in\mathbb{Z}} a_{n,m} e^{2\pi i(nx+my)}$$
with only finitely many nonzero $a_{n,m}$. If $u=v-\Delta v$ where $\Delta = \partial_x^2 + \partial_y^2$ is the Laplacian, prove that
$$||v||_{L^\infty([0,1]^2)} \le C||u||_{L^2([0,1]^2)}$$
for some constant $C$ independent of $v$.
:::
