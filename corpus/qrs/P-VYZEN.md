---
schema: qual/card@1
id: P-VYZEN
kind: problem
title: $[F_q(\omega):F_q]$ is the multiplicative order of $q$ modulo $n$
classification:
  areas:
  - algebra
  topics:
  - finite-fields
  - roots-of-unity
  - cyclic-groups
relations: []
review: draft
solved: true
---
Let $F$ be a finite field with $q$ elements.
Let $n$ be a positive integer relatively prime to $q$ and let $\omega$ be a primitive $n$th root of unity in an extension field of $F$.
Let $E = F [\omega]$ and let $k = [E : F]$.

a.
Prove that $n$ divides $q^{k}-1$.

b. 
Let $m$ be the order of $q$ in $\ZZ/n\ZZ\units$.
Prove that $m$ divides $k$.

c.
Prove that $m = k$.

:::{.concept}
\envlist

- $\FF\units$ is always cyclic for $\FF$ a field.
- Lagrange: $H\leq G \implies \#H \divides \# G$.

:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Since $\abs{F} = q$ and $[E:F] = k$, we have $\abs{E} = q^k$ and $\abs{E\units} = q^k-1$.

- Noting that $\omega \in E\units$ we must have $n = o(\omega) \divides \abs{E\units} = q^k-1$ by Lagrange's theorem.

:::

:::{.proof title="of b"}
\envlist

- Rephrasing (a), we have 
\[
n \divides q^k-1 
&\iff q^k-1 \cong 0 \mod n \\
&\iff q^k \cong 1 \mod n \\
&\iff m \definedas o(q) \divides k
.\]

:::

:::{.proof title="of c"}
\envlist

- Write $k = \ell m$, which is possible since $m \divides k$ by part (b).
  The subfields of $E$ containing $F$ correspond to the divisors of $k = [E:F]$, so there is an intermediate field $M$ with
\[
F \leq M \leq E \quad\text{and}\quad k = [E:F] = [E:M] [M:F] = \ell \cdot m
,\]

  so $M$ is a degree $m$ extension of $F$ and $\abs{M} = q^m$.

- Now consider $M\units$. 
- By the argument in (a), $n$ divides $q^m - 1 = \abs{M\units}$, and $M\units$ is cyclic, so it contains a cyclic subgroup $H$ of order $n$.

- Every $x\in H$ satisfies $p(x) = 0$ for $p(x)\definedas x^n-1$, and $p$ has at most $n$ roots in a field, so those $n$ elements are all of them. 

- So $H = \theset{x \in M \suchthat x^n-1 = 0}$, i.e. $H$ is exactly the set of solutions to $x^n = 1$ in $M$.

- But $\omega$ is one such solution, so $\omega \in H \subseteq M\units \subseteq M$.

- Since $E = F[\omega]$ is the smallest field containing $F$ and $\omega$, and $M$ is a field containing both, we get $E \subseteq M$.
  Together with $M \subseteq E$ this gives $M = E$, so $\ell = 1$ and $k = m$.

:::

:::
