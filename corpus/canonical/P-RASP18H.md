---
schema: qual/card@1
id: P-RASP18H
kind: problem
title: "Banach limit extension and non-representability by l^1"
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
Let $\ell^\infty(\mathbb{N})$ be the Banach space of bounded complex sequences $x = (x_1, x_2, x_3, \ldots)$ such that $\|x\|_\infty = \sup_n |x_n| < \infty$ and let $V$ be the subspace defined as:
$$
V = \left\{x \in \ell^\infty(\mathbb{N}) : \lim_{n \to \infty} \frac{1}{n}(x_1 + x_2 + \cdots + x_n) \text{ exists in } \mathbb{C}\right\}.
$$

1. Prove that there exists $\varphi \in \ell^\infty(\mathbb{N})^*$ such that $\varphi(x) = \lim_{n \to \infty} \frac{1}{n}(x_1 + x_2 + \cdots + x_n)$ for every $x \in V$.

Let $\psi \in \ell^\infty(\mathbb{N})^*$ be any continuous linear functional such that $\psi(x) = \lim_{n \to \infty} \frac{1}{n}(x_1 + x_2 + \cdots + x_n)$ when $x \in V$.

2. Show $\psi(\tilde{x}) = \psi(x)$ for every $x = (x_1, x_2, x_3, x_4, \ldots) \in \ell^\infty(\mathbb{N})$ where $\tilde{x} := (x_2, x_3, x_4, \ldots)$.

3. Show there is no $y \in \ell^1(\mathbb{N})$ such that $\psi(x) = \sum_{n=1}^{\infty} x_n y_n$ for all $x \in \ell^\infty(\mathbb{N})$.
:::
