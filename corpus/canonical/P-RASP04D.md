---
schema: qual/card@1
id: P-RASP04D
kind: problem
title: "Differentiation and approximation properties of convolution"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $\varphi \in C_c^\infty(\mathbb{R})$ and $f : \mathbb{R} \to \mathbb{R}$ be an absolutely continuous function with compact support, and $\varphi * f$ be the convolution of $\varphi$ and $f$:
$$
(\varphi * f)(x) := \int_{\mathbb{R}} \varphi(x - y) f(y)\,dy.
$$

(a) Show $\frac{d}{dx}(\varphi * f)(x) = (\varphi' * f)(x)$ for all $x \in \mathbb{R}$.

(b) Show $(\varphi' * f)(x) = (\varphi * f')(x)$ for all $x \in \mathbb{R}$.

(c) Explain why there exists $f_n \in C_c^\infty(\mathbb{R})$ such that
$$
\lim_{n \to \infty} \|f_n - f\|_{L^\infty(\mathbb{R}, m)} = 0 = \lim_{n \to \infty} \|f' - f_n'\|_{L^1(\mathbb{R}, m)}.
$$
:::
