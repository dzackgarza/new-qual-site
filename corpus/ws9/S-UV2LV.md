---
schema: qual/card@1
id: S-UV2LV
kind: solution
title: Solution to P-I67ZI
classification:
  areas:
  - real-analysis
  topics: []
relations:
- kind: solves
  target: P-I67ZI
review: draft
---

:::{.solution}
(1) easy to verify.

(2) For $y\in Y$, by definition of $|||\cdot|||$, $|||y|||\le\|y\|$.

In the converse, choose a $\phi\in (Y,\|\cdot\|)^*$, s.t. $\phi(y)=\|y\|$ and norm of $\phi$ is 1. Thus for all $y\in Y$, $|\phi(y)|\le\|y\|\le C\|y\|$. Then, $\phi$ can be extent to whole $X$ with the same norm, say for all $x\in X$, $|\phi(x)|\le C\|x\|$. Then $\phi\in S$ and thus $|||y|||\ge\|y\|$.

(3) By def of $|||\cdot|||$, $|||x|||\le C\|x\|$. In the converse, for all $x\in X$, by Hahn-Banach theorem, there is a $\phi$ s.t. $\phi(x)=\|x\|$, and $\|\phi\|=1$. Define $\psi=\frac{1}{C}\phi$, which implies that $\psi(x)=\frac1C\|x\|$ and $|\psi(z)|\le\frac1C\|z\|\le C\|z\|$ for all $z\in X$ while $|\psi(y)|\le\frac1C\|y\|\le\|y\|$ for all $y\in Y$. Thus $\psi\in S$ and thus $|||x|||\ge\frac1C\|x\|$.
:::
