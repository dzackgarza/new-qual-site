---
schema: qual/card@1
id: P-6Y3IL
kind: problem
title: "Suppose that $f_j \\in L^2(\\mathbb{R}^d)$, $j = 1, 2, \\ldots$, and $f \\in L^2(\\mathbb{R}^d)$ satisfy $\\lim_{j\\to\\infty} \\int_{\\mathbb{R}^d} f_j g = \\int_{\\mathbb{R}^d} fg$ for all $g \\in L^2(\\mathbb{R}^d)$."
classification:
  areas:
  - real-analysis
  topics:
  - weak-convergence
  - l2
  - hilbert-spaces
relations: []
review: draft
---

::: {.problem title="?"}
Suppose that $f_j \in L^2(\mathbb{R}^d)$, $j = 1, 2, \ldots$, and $f \in L^2(\mathbb{R}^d)$ satisfy $$\lim_{j\to\infty} \int_{\mathbb{R}^d} f_j g = \int_{\mathbb{R}^d} fg$$ for all $g \in L^2(\mathbb{R}^d)$.
That is, $f_j$ converges to $f$ weakly in $L^2$.
Suppose that the sequence satisfies the uniform bound $$\sup_{x\in\mathbb{R}^d}(1+|x|)^d|f_j(x)| \le M < \infty. \qquad (A)$$

Show that $\|f_j\|_2 \to \|f\|_2$ and conclude that $\|f_j - f\|_2 \to 0$.
That is $f_j$ converges to $f$ strongly in $L^2(\mathbb{R}^d)$.
Show by example that condition (A) is necessary.
:::
