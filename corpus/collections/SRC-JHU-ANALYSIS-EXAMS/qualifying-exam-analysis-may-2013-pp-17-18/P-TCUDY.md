---
schema: qual/card@1
id: P-TCUDY
kind: problem
title: 'Weak convergence plus norm convergence implies strong convergence in $L^2$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
---

Recall that the inner product on $L^2(\mathbb{R}^d)$ is given by

$$(f, g) = \int_{\mathbb{R}^d} f(x) \overline{g(x)} \, dx, \quad \text{for } f, g \in L^2(\mathbb{R}^d),$$

which induces the $L^2$-norm

$$\|f\|_{L^2} = (f, f)^{1/2}.$$

(a) If the sequence of functions $\{f_n\}_{n=1}^\infty$ in $L^2(\mathbb{R}^d)$ satisfy that $\|f_n\|_{L^2} = 1$, show that there exists a subsequence of functions $\{f_{n_j}\}_{j=1}^\infty$ such that $f_{n_j}$ converges weakly to some function $f$ in $L^2(\mathbb{R}^d)$, i.e.,

$$(f_{n_j}, g) \to (f, g) \quad \text{for all } g \in L^2(\mathbb{R}^d).$$

(b) If $f_n \rightharpoonup f$ weakly in $L^2(\mathbb{R}^d)$ and $\|f_n\|_{L^2} \to \|f\|_{L^2}$ as $n \to \infty$, show that $\|f_n - f\|_{L^2} \to 0$ as $n \to \infty$.
