---
schema: qual/card@1
id: P-G5MEU
kind: problem
title: Degree, Galois group, and intermediate fields of $\QQ(\sqrt{2}+\sqrt{5})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $K = \QQ[\sqrt 2 + \sqrt 5]$.

a. Find $[K: \QQ]$.

b. Show that $K/\QQ$ is Galois, and find the Galois group $G$ of $K/\QQ$.

c. Exhibit explicitly the correspondence between subgroups of $G$ and intermediate fields between $\QQ$ and $K$.
:::

::: solution
Put
\[
\theta=\sqrt2+\sqrt5.
\]
Then
\[
\theta^2=7+2\sqrt{10},
\qquad
\sqrt{10}=\frac{\theta^2-7}{2}\in\mathbb Q(\theta).
\]
Moreover
\[
\theta\sqrt{10}=5\sqrt2+2\sqrt5,
\]
so subtracting $2\theta$ gives
\[
3\sqrt2=\theta(\sqrt{10}-2).
\]
Hence $\sqrt2\in\mathbb Q(\theta)$, and then $\sqrt5=\theta-\sqrt2\in\mathbb Q(\theta)$. Thus
\[
K=\mathbb Q(\theta)=\mathbb Q(\sqrt2,\sqrt5).
\]
Since $\sqrt5\notin\mathbb Q(\sqrt2)$, the degree is
\[
[K:\mathbb Q]=4.
\]

The field contains all four conjugates
\[
\pm\sqrt2\pm\sqrt5
\]
of $\theta$, so $K/\mathbb Q$ is Galois. Its automorphisms independently change the signs of $\sqrt2$ and $\sqrt5$, giving
\[
G\cong C_2\times C_2.
\]
Let $\sigma_2$ change the sign of $\sqrt2$ and fix $\sqrt5$, and let $\sigma_5$ change the sign of $\sqrt5$ and fix $\sqrt2$. Then the Galois correspondence is
\[
\begin{array}{c|c}
H&K^H\\ \hline
G&\mathbb Q\\
\langle\sigma_2\rangle&\mathbb Q(\sqrt5)\\
\langle\sigma_5\rangle&\mathbb Q(\sqrt2)\\
\langle\sigma_2\sigma_5\rangle&\mathbb Q(\sqrt{10})\\
\{1\}&K.
\end{array}
\]
These are all subgroups of $G$ and hence all intermediate fields.
:::
