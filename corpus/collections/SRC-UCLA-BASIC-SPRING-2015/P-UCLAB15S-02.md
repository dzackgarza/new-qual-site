---
schema: qual/card@1
id: P-UCLAB15S-02
kind: problem
title: Compact embedding between Hölder spaces
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$. We say that $f$ is Hölder continuous of order $\alpha\in(0,1)$ and write $f\in C^\alpha([0,1])$ if
\[
\|f\|_{C^\alpha}
:=\sup_{x\in[0,1]}|f(x)|
+\sup_{\substack{x,y\in[0,1]\\x\ne y}}
\frac{|f(x)-f(y)|}{|x-y|^\alpha}<\infty.
\]
This defines a norm on $C^\alpha([0,1])$. Prove that any bounded sequence in $C^{1/2}([0,1])$ admits a convergent subsequence in $C^{1/3}([0,1])$.
:::
