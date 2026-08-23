---
schema: qual/card@1
id: P-RASP08D
kind: problem
title: "Banach limit extension of Cesaro mean functional"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $\ell^\infty$ denote the Banach space of all bounded real-valued functions on $\mathbb{N}$, and $f_n$ the bounded linear functional
$$
f_n(x) := \frac{x(1) + \ldots + x(n)}{n}.
$$
Let $M \subset \ell^\infty$ be the subspace of all $x$ such that $\lim_{n \to \infty} f_n(x)$ exists, and $f$ the linear functional $M \to \mathbb{R}$ given by $f(x) := \lim_{n \to \infty} f_n(x)$.

(a) Let $\tau : \ell^\infty \to \ell^\infty$ denote the shift operator given by $(\tau x)(n) = x(n+1)$ for $n = 1, 2, \ldots$. Show that $\tau$ sends $M$ to $M$ and $f(\tau x) = f(x)$ for all $x \in M$.

(b) Show that there is a linear functional $F : \ell^\infty \to \mathbb{R}$ such that $F|_M = f$ and
$$
\liminf_{n \to \infty} x(n) \leq F(x) \leq \limsup_{n \to \infty} x(n).
$$
:::
