---
schema: qual/card@1
id: P-7Q1AX
kind: problem
title: '**Lemma:**'
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

**Lemma:** If $x \divides n$ and $x\divides m$ then $x\divides \gcd(m, n)$

*Proof:* We have $x\divides km + \ell n$ for any integers $k, \ell$.
So let $d = \gcd(m, n)$, then there exist integers $a, b$ such that $am + bn = d$.
But we can now just take $k=a$ and $\ell = b$.
$\qed$

We claim that $\ZZ_n[m] \cong \ZZ_{(m, n)}$, from which the result immediately follows by part 1.

Define a map
\[
\begin{align*}
\phi: \ZZ &\to \ZZ_n[m] \\ 
1 &\mapsto [1]_{\mod n}
,\end{align*}
\]

which we claim is an isomorphism.
$\phi$ is clearly surjective since $\ZZ\to \ZZ_n$ is a quotient map and $\ZZ_n[m]$ is a subgroup of $\ZZ_n$, and if we let $d \definedas \gcd(m, n)$, we have

\[
\begin{align*}
\ker \phi &= \theset{x\in \ZZ_n \suchthat  mx = 0} \\
&= \theset{x \in \ZZ_n \suchthat x \divides m} \\
&= \theset{x \in \ZZ \suchthat x \divides n ~\text{ and }~ x \divides m} \\
&= \theset{x \in \ZZ \suchthat x \divides d} \quad \text{by the lemma} \\
&= d\ZZ~
.\end{align*}
\]

Then by the first isomorphism theorem, we have
$$
\frac{\ZZ}{\ker \phi} \cong \im \phi \implies \frac{\ZZ}{d\ZZ} \cong \ZZ_n[m].
$$
