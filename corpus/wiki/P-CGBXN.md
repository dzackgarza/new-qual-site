---
schema: qual/card@1
id: P-CGBXN
kind: problem
title: "Let $F$ be a finite field with $q$ elements. Let $n$ be a positive\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
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
- Lagrange: $H\leq G \implies \size H \divides \size G$.

:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Since $\abs{F} = q$ and $[E:F] = k$, we have $\abs{E} = q^k$ and $\abs{E\units} = q^k-1$.

- Noting that $\zeta \in E\units$ we must have $n = o(\zeta) \divides \abs{E\units} = q^k-1$ by Lagrange's theorem.

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

- Since $m\divides k \iff k = \ell m$, (**claim**) there is an intermediate subfield $M$ such that
\[
E \leq M \leq F \quad k = [F:E] = [F:M] [M:E] = \ell m
,\]

  so $M$ is a degree $m$ extension of $E$.

- Now consider $M\units$. 
- By the argument in (a), $n$ divides $q^m - 1 = \abs{M\units}$, and $M\units$ is cyclic, so it contains a cyclic subgroup $H$ of order $n$.

- But then $x\in H \implies p(x)\definedas x^n-1 = 0$, and since $p(x)$ has at most $n$ roots in a field. 

- So $H = \theset{x \in M \suchthat x^n-1 = 0}$, i.e. $H$ contains all solutions to $x^n-1$ in $E[x]$.

- But $\zeta$ is one such solution, so $\zeta \in H \subset M\units \subset M$.

- Since $F[\zeta]$ is the smallest field extension containing $\zeta$, we must have $F = M$, so $\ell = 1$, and $k = m$.

:::

:::

