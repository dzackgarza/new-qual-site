---
schema: qual/card@1
id: P-7Q1AX
kind: problem
title: "Lemma: If $x \\divides n$ and $x\\divides m$ then $x\\divides \\gcd(m, n)$"
classification:
  areas:
  - algebra
  topics:
  - cyclic-groups
  - isomorphism-theorems
  - number-theory
relations: []
review: draft
---

::: problem
**Lemma:** If $x \divides n$ and $x\divides m$ then $x\divides \gcd(m, n)$

*Proof:* We have $x\divides km + \ell n$ for any integers $k, \ell$.
So let $d = \gcd(m, n)$, then there exist integers $a, b$ such that $am + bn = d$.
But we can now just take $k=a$ and $\ell = b$.
$\qed$

We claim that $\ZZ_n[m] \cong \ZZ_{(m, n)}$, from which the result immediately follows by part 1.

Let $d \definedas \gcd(m,n)$ and define a map
\[
\begin{align*}
\phi: \ZZ &\to \ZZ_n \\ 
1 &\mapsto [n/d]_{\mod n}
.\end{align*}
\]

Note that $1\mapsto [1]$ would not work: $[1]$ is not $m\dash$torsion unless $n\divides m$.

**The image is exactly $\ZZ_n[m]$.** First, $m\cdot (n/d) = (m/d)n \equiv 0 \mod n$, so $\im \phi \subseteq \ZZ_n[m]$.
Conversely, suppose $[x] \in \ZZ_n[m]$, so $n \divides mx$.
Dividing by $d$ gives $(n/d) \divides (m/d)x$, and $\gcd(n/d, m/d) = 1$, so $(n/d)\divides x$.
Hence $[x] \in \gens{[n/d]} = \im\phi$.

**The kernel is $d\ZZ$.**
\[
\begin{align*}
\ker \phi &= \theset{x\in \ZZ \suchthat (n/d)x \equiv 0 \mod n} \\
&= \theset{x \in \ZZ \suchthat n \divides (n/d) x} \\
&= \theset{x \in \ZZ \suchthat d \divides x} \\
&= d\ZZ~
.\end{align*}
\]

Then by the first isomorphism theorem, we have
$$
\frac{\ZZ}{\ker \phi} \cong \im \phi \implies \frac{\ZZ}{d\ZZ} \cong \ZZ_n[m].
$$
:::
