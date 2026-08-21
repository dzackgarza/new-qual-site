---
schema: qual/card@1
id: P-7Y4VS
kind: problem
title: 'Holomorphic $L^2$ functions: $\sup_K|f|\le C_K\|f\|_{L^2}$, the $L^2$ unit
  ball is a normal family, and $L^2$ singularities at $0$ are removable'
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - Normal Families
  - L²
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $U$ be an open subset of $\mathbb{C}$.
We use the notion $$\|f\|_{L^2(U)} = \left(\int_U |f|^2 dxdy\right)^{1/2}.$$

- Let $f : U \to \mathbb{C}$ be a holomorphic function.
  Show that for any compact set $K \subset U$, there is a constant $C_K$, such that $$\sup_{z\in K}|f(z)| \le C_K \|f\|_{L^2(U)}.$$

- Prove that $\{f \text{ holomorphic on } U : \|f\|_{L^2(U)} \le 1\}$ is a normal family.

- Suppose $U$ is the punctured disc $D(0,1) - \{0\}$.
  If $f$ is holomorphic on $U$ and $\|f\|_{L^2(U)} < \infty$, prove that $z = 0$ is a removable singularity of $f$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $U \subseteq \CC$ open and holomorphic $f$: (i) $\sup_K |f| \le C_K \|f\|_{L^2(U)}$ for compact $K \subset U$; (ii) $\{f \text{ holomorphic} : \|f\|_{L^2(U)} \le 1\}$ is a normal family; (iii) if $U = D(0,1) \setminus \{0\}$ and $f$ is holomorphic with $\|f\|_{L^2(U)} < \infty$, then $0$ is a removable singularity.

<1>1. Mean-value inequality: for $\overline{D(a,r)} \subset U$, $|f(a)| \le \frac{1}{\sqrt{\pi} r} \|f\|_{L^2(D(a,r))}$.
Proof: by the mean value property $f(a) = \frac{1}{\pi r^2}\int_{D(a,r)} f\, dA$, so $|f(a)| \le \frac{1}{\pi r^2}\int_{D(a,r)} |f| \, dA \le \frac{1}{\pi r^2} \cdot \sqrt{\pi r^2}\, \|f\|_{L^2(D(a,r))}$ by Cauchy--Schwarz.

<1>2. (i) For compact $K \subset U$, $\sup_K |f| \le C_K \|f\|_{L^2(U)}$.
Proof: choose $r > 0$ with $\overline{D(a,r)} \subset U$ for all $a \in K$ (e.g. $r = \frac{1}{2}\dist(K, \bd U)$; if $U = \CC$ take any fixed $r$ and cover $K$). Cover $K$ by finitely many disks $D(a_j, r/2)$; then <1>1 applied on $D(a_j, r)$ gives $|f(z)| \le \frac{1}{\sqrt\pi r}\|f\|_{L^2(U)}$ for every $z \in K$, so $C_K = 1/(\sqrt\pi\, r)$ works.

<1>3. (ii) The unit ball $\mcf = \{f \text{ holomorphic on } U : \|f\|_{L^2(U)} \le 1\}$ is normal.
Proof: by <1>2, $\sup_K |f| \le C_K$ for all $f \in \mcf$; hence $\mcf$ is locally bounded, so by Montel's theorem it is normal.

<1>4. (iii) Setup: write the Laurent expansion $f(z) = \sum_{n \in \ZZ} c_n z^n$ on $D(0,1) \setminus \{0\}$.
Proof: existence of the Laurent series is standard.

<1>5. $\|f\|_{L^2}^2 = 2\pi \sum_{n \in \ZZ} |c_n|^2 \int_0^1 r^{2n+1}\, dr$ (allowing $+\infty$). Proof: in polar coordinates $\int_{D(0,1)\setminus\{0\}} |f|^2\, dA = \int_0^1 \int_0^{2\pi} |f(re^{i\theta})|^2\, d\theta\, r\, dr$, and by orthogonality of $\{e^{in\theta}\}$, $\int_0^{2\pi}|f(re^{i\theta})|^2 d\theta = 2\pi \sum_n |c_n|^2 r^{2n}$ (Parseval); use monotone convergence to interchange sum and integral.

<1>6. $c_n = 0$ for all $n < 0$.
Proof: for $n \le -1$, $\int_0^1 r^{2n+1}\, dr = \infty$; since $\|f\|_{L^2} < \infty$, <1>5 forces $c_n = 0$ for every $n \le -1$.

<1>7. $0$ is a removable singularity.
Proof: by <1>6, $f(z) = \sum_{n \ge 0} c_n z^n$ on $D(0,1) \setminus \{0\}$, which is the restriction of a power series convergent on $D(0,1)$; hence $f$ extends holomorphically to $0$.

<1>8. Q.E.D. Proof: <1>2, <1>3, and <1>4–<1>7 prove (i), (ii), (iii) respectively.
:::
