---
schema: qual/card@1
id: P-RAF04F
kind: problem
title: "L^1 convergence of derivatives implies absolute continuity of the limit"
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
  - L1 Convergence
  - Fundamental Theorem of Calculus
relations: []
review: draft
---

::: problem
Let $f_n : \mathbb{R} \to \mathbb{R}$ be a sequence of absolutely continuous functions such that $f_n' \in L^1(\mathbb{R}, m)$ and $c := \lim_{n \to \infty} f_n(0)$ exists in $\mathbb{R}$.
Further assume there exists $g \in L^1(\mathbb{R}, m)$ such that $\lim_{n \to \infty} \int_\mathbb{R} |g(x) - f_n'(x)| \, dx = 0$.

(a) Show that $f(x) := \lim_{n \to \infty} f_n(x)$ exists for all $x \in \mathbb{R}$.

(b) Show that $f$ is absolutely continuous and $f'(x) = g(x)$ for $m$-a.e. $x$.
:::
