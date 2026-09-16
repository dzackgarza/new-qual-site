---
schema: qual/card@1
id: P-CAS24E
kind: problem
title: "Polynomials with $p_n(0)=1$, $p_n'(0)=0$, pointwise tending to $0$ off $0$"
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomials
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Show that there exist polynomials $p_n$ such that

(i) $p_n(0) = 1$, $p_n'(0) = 0$,

(ii) $p_n(z) \to 0$ as $n \to \infty$ for all fixed $z \in \mathbb{C} \setminus \{0\}$.
:::

::: {.solution}
Choose pairwise disjoint open arcs $I_n\subset\mathbb T$. Define
\[
K_n=
\left\{z:\frac1n\le |z|\le n,
\ \frac z{|z|}\notin I_n\right\}
\]
and
\[
L_n=K_n\cup \overline{D\!\left(0,\frac1{2n}\right)}.
\]
The complement of $L_n$ is connected: the annular gap around the small disk
connects to the exterior through the radial corridor determined by $I_n$.

Define a function $h_n$ on $L_n$ by
\[
h_n=0\text{ on }K_n,
\qquad
h_n=1\text{ on }\overline{D\!\left(0,\frac1{2n}\right)}.
\]
It is continuous on $L_n$ and holomorphic in its interior. By Mergelyan's
theorem, for any $\varepsilon_n>0$ there is a polynomial $q_n$ with
\[
\sup_{L_n}|q_n-h_n|<\varepsilon_n.
\]
Choose $\varepsilon_n$ so small that
\[
\varepsilon_n\to0,
\qquad
n^2\varepsilon_n\to0.
\]
Because $q_n$ is $\varepsilon_n$-close to the constant $1$ on
$|z|\le1/(2n)$, Cauchy's estimate gives
\[
|q_n'(0)|\le 2n\varepsilon_n,
\qquad
|q_n(0)-1|\le\varepsilon_n.
\]
For large $n$ define
\[
p_n(z)=\frac{q_n(z)-q_n'(0)z}{q_n(0)}.
\]
Then exactly
\[
p_n(0)=1,
\qquad
p_n'(0)=0.
\]

Now fix $z\ne0$. For all sufficiently large $n$ we have
$1/n\le|z|\le n$. Since the arcs $I_n$ are pairwise disjoint, the direction
$z/|z|$ belongs to at most one of them. Hence $z\in K_n$ for all sufficiently
large $n$. On $K_n$,
\[
|q_n(z)|\le\varepsilon_n,
\qquad
|q_n'(0)z|\le2n\varepsilon_n|z|.
\]
Both terms tend to $0$, while $q_n(0)\to1$. Therefore
\[
p_n(z)\longrightarrow0
\]
for every fixed $z\ne0$.
:::
