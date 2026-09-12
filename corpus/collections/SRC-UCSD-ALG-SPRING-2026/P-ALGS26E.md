---
schema: qual/card@1
id: P-ALGS26E
kind: problem
title: "Projective modules from ideal equations"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Suppose $D$ is a Noetherian integral domain, $F$ is the field of fractions of $D$, $\mathfrak{a} \subseteq D$ is an ideal of $D$, and $M$ is a finitely generated $D$-submodule of $F$.
Suppose $\mathfrak{a}M = D$, where
$$
\mathfrak{a}M = \left\{\sum_{i=1}^{n} c_i x_i \mid c_i \in \mathfrak{a},\; x_i \in M\right\}.
$$

(a) Prove that $M$ is projective.

(b) Prove that $\mathfrak{a} \otimes_D M \cong D$.
:::

::: {.solution}
<1>1. Since \(\mathfrak aM=D\), there exist \(c_1,\dots,c_r\in\mathfrak a\) and \(x_1,\dots,x_r\in M\) such that
\[
\sum_{i=1}^r c_i x_i=1.
\]
::: {.proof}
This is exactly the assertion \(1\in\mathfrak aM\), using the definition of the product \(\mathfrak aM\) in the problem.
:::

<1>2. For each \(i\), define a \(D\)-linear map
\[
\varphi_i:M\longrightarrow D,
\qquad
\varphi_i(m)=c_i m.
\]
::: {.proof}
Because \(c_i\in\mathfrak a\) and \(m\in M\), the product \(c_i m\) belongs to \(\mathfrak aM=D\). Thus \(\varphi_i\) is well-defined.
It is \(D\)-linear because multiplication takes place in the fraction field \(F\), which is commutative.
:::

<1>3. For every \(m\in M\),
\[
m=\sum_{i=1}^r x_i\varphi_i(m).
\]
::: {.proof}
Using <1>1,
\[
\sum_{i=1}^r x_i\varphi_i(m)
 =\sum_{i=1}^r x_i(c_i m)
 =m\sum_{i=1}^r c_i x_i
 =m.
\]
:::

<1>4. The module \(M\) is projective.
::: {.proof}
The finite families \(x_1,\dots,x_r\in M\) and \(\varphi_1,\dots,\varphi_r\in\operatorname{Hom}_D(M,D)\) satisfy the dual-basis identity of <1>3. By the dual-basis criterion for projectivity, \(M\) is projective.
This proves part (a).
:::

<1>5. Let
\[
\mu:\mathfrak a\otimes_D M\longrightarrow D,
\qquad
\mu(c\otimes m)=cm.
\]
Then \(\mu\) is a well-defined surjective \(D\)-linear map.
::: {.proof}
The multiplication map \(\mathfrak a\times M\to D\), \((c,m)\mapsto cm\), is \(D\)-balanced, so it induces \(\mu\). Its image is precisely \(\mathfrak aM=D\), hence it is surjective.
:::

<1>6. Define a \(D\)-linear map
\[
\nu:D\longrightarrow\mathfrak a\otimes_D M,
\qquad
\nu(d)=d\sum_{i=1}^r c_i\otimes x_i.
\]
Then \(\mu\circ\nu=\operatorname{id}_D\).
::: {.proof}
By <1>1,
\[
\mu(\nu(d))
 =d\sum_{i=1}^r c_i x_i
 =d.
\]
:::

<1>7. For every pure tensor \(c\otimes m\in\mathfrak a\otimes_D M\), one has
\[
\nu(\mu(c\otimes m))=c\otimes m.
\]
::: {.proof}
Since \(c_i m\in D\) for every \(i\), the tensor relations give
\[
\begin{aligned}
\nu(cm)
 &=cm\sum_{i=1}^r c_i\otimes x_i\\
 &=\sum_{i=1}^r c\otimes (c_i m)x_i\\
 &=c\otimes\left(\sum_{i=1}^r (c_i m)x_i\right)\\
 &=c\otimes m,
\end{aligned}
\]
where the last equality is <1>3 applied to \(m\).
:::

<1>8. Therefore \(\mu\) and \(\nu\) are inverse isomorphisms, so
\[
\mathfrak a\otimes_D M\cong D.
\]
::: {.proof}
By <1>6, \(\mu\nu=\operatorname{id}_D\). By <1>7 and linearity, \(\nu\mu\) is the identity on every tensor, since pure tensors generate \(\mathfrak a\otimes_D M\). This proves part (b).
:::
:::
