---
schema: qual/card@1
id: P-LZVDM
kind: problem
title: 'Let $K$ be a field. A discrete valuation on $K$ is a function $\nu:'
classification:
  areas:
  - algebra
  topics:
  - fields
  - rings
  - commutative-algebra
relations: []
review: draft
---

::: problem
Let $K$ be a field. A discrete valuation on $K$ is a function $\nu:
K\setminus\{0\}\rightarrow\mathbb Z$ such that

-   $\nu(ab)=\nu(a)+\nu(b)$

-   $\nu$ is surjective

-   $\nu(a+b)\geq\text{min}\{(\nu(a),\nu(b)\}$ for
    $a,b\in K\setminus\{0\}$ with $a+b\neq 0$.

Let $R:=\{x\in K\setminus\{0\}:\nu(x)\geq0\}\cup\{0\}$. Then
$R$ is called the valuation ring of $\nu$.

Prove the following:

-   $R$ is a subring of $K$ containing the 1 in $K$.

-   for all $x\in K\setminus\{0\}$, either $x$ or
    $x\inv$ is in $R$.

-   $x$ is a unit of $R$ if and only if $\nu(x)=0$.

-   Let $p$ be a prime number, $K=\mathbb Q$,
    and $\nu_p:\mathbb Q\setminus\{0\}\rightarrow\mathbb Z$
    be the function defined by $\nu_p(\frac ab)=n$ where
    $\frac ab=p^n\frac cd$ and $p$ does not divide $c$ and $d$.
    Prove that the corresponding valuation ring $R$ is the ring
    of all rational numbers whose denominators are relatively
    prime to $p$.
:::
