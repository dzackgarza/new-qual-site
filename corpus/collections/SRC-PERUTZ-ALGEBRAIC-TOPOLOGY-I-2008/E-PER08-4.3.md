---
schema: qual/card@1
id: E-PER08-4.3
kind: problem
title: Five models of the 3-strand braid group and the trefoil group
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 4.3 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
---

::: {.problem}
Let $K\subset S^3$ be the left-handed trefoil knot.
This exercise compares the following groups:

- $\pi_1(S^3\setminus K)$;

- $\langle a,b\mid a^2=b^3\rangle$;

- $\langle s,t\mid sts=tst\rangle$;

- the geometric braid group $B_3=\pi_1(C_3)$, where $C_3$ is the configuration space of unordered $3$-element subsets of $\mathbb C$;

- $\pi_1(\mathbb C^2\setminus C)$, where $C=\{(X,Y):X^2=Y^3\}$ is the cuspidal cubic.

1. Show that $a\mapsto sts$ and $b\mapsto ts$ define an isomorphism
   \[
   \langle a,b\mid a^2=b^3\rangle\xrightarrow{\sim}\langle s,t\mid sts=tst\rangle.
   \]

2. With basepoint $\{-2,0,2\}\in C_3$, define loops
   \[
   \sigma(t)=\{-1-e^{\pi it},-1+e^{\pi it},2\},\qquad
   \tau(t)=\{-2,1-e^{\pi it},1+e^{\pi it}\}.
   \]
   If $s=[\sigma]$ and $t=[\tau]$, check that $sts=tst$, obtaining a homomorphism $\langle s,t\mid sts=tst\rangle\to B_3$.

3. Let $\operatorname{Sym}^3_0(\mathbb C)$ be the unordered triples $\{a,b,c\}$ with $a+b+c=0$.
   Show that
   \[
   \operatorname{Sym}^3(\mathbb C)\cong \mathbb C\times\operatorname{Sym}^3_0(\mathbb C),
   \]
   and define a homeomorphism $\operatorname{Sym}^3_0(\mathbb C)\to\mathbb C^2$ by sending $\{a,b,c\}$ to $(x,y)$ such that
   \[
   (t-a)(t-b)(t-c)=t^3+xt+y.
   \]
   Verify that $a,b,c$ are distinct if and only if $4x^3+27y^2\ne0$.
   Deduce that
   \[
   C_3\cong\mathbb C\times(\mathbb C^2\setminus C)
   \]
   and hence $B_3\cong\pi_1(\mathbb C^2\setminus C)$.

4. Show that $\mathbb C^2\setminus C$ is homotopy equivalent to $S^3\setminus K$.

5. Show that going around the resulting circle of homomorphisms gives an automorphism of $\pi_1(S^3\setminus K)$.
:::
