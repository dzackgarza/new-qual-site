---
schema: qual/card@1
id: E-SS3.PR-5
kind: problem
title: The Cauchy integral of a function on an interval, and its jump
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral
  - Boundary Behaviour
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Chapter 3, §9, problem 5, read from
    `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF page 129). This card did not
    exist before: it was found missing by a completeness audit of the collection against the book,
    which located every printed Exercises and Problems item and compared it with the cards on disk.
    The transcription was taken from the OCR text layer and cleaned of OCR errors; the asterisk marking a starred problem, and the
    printed wording, hypotheses and bracketed hints are preserved.
---

::: {.exercise}
Let
$$
g(z)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{h(x)}{x-z}\,dx
$$
where $h$ is continuous and supported in $[-M,M]$.

(a) Prove that the function $g$ is holomorphic in $\CC\setminus[-M,M]$, and vanishes at infinity, that is, $\lim_{\abs z\to\infty}\abs{g(z)}=0$. Moreover, the "jump" of $g$ across $[-M,M]$ is $h$, that is,
$$
h(x)=\lim_{\epsilon\to0,\ \epsilon>0}g(x+i\epsilon)-g(x-i\epsilon).
$$
[Hint: Express the difference $g(x+i\epsilon)-g(x-i\epsilon)$ in terms of a convolution of $h$ with the Poisson kernel.]

(b) If $h$ satisfies a mild smoothness condition, for instance a H\"older condition with exponent $\alpha$, that is, $\abs{h(x)-h(y)}\le C\abs{x-y}^{\alpha}$ for some $C>0$ and all $x,y\in[-M,M]$, then $g(x+i\epsilon)$ and $g(x-i\epsilon)$ converge uniformly to functions $g^+(x)$ and $g^-(x)$ as $\epsilon\to0$. Then $g$ can be characterized as the unique holomorphic function that satisfies:

(i) $g$ is holomorphic outside $[-M,M]$,

(ii) $g$ vanishes at infinity,

(iii) $g(x+i\epsilon)$ and $g(x-i\epsilon)$ converge uniformly as $\epsilon\to0$ to functions $g^+(x)$ and $g^-(x)$ with
$$
g^+(x)-g^-(x)=h(x).
$$
[Hint: If $G$ is another function satisfying these conditions, $g-G$ is entire.]
:::

