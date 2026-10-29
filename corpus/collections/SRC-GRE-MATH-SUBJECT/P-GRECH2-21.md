---
schema: qual/card@1
id: P-GRECH2-21
kind: problem
title: Local maximum of $\int_x^{2x}\sin t/t\,dt$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 21 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
The following function is defined for all positive $x$:

$$
f(x) = \int_{x}^{2x} \frac{\sin t}{t} dt
$$

At what value of $x$ on the interval $(0, \frac{3\pi}{2})$ does this function attain a local maximum?

(A) $\frac{\pi}{6}$
(B) $\frac{\pi}{3}$
(C) $\frac{\pi}{2}$
(D) $\pi$
(E) $\frac{2\pi}{3}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x>0$,
$$
f'(x)=\frac{\sin 2x-\sin x}{x}
=\frac{\sin x(2\cos x-1)}{x}.
$$


::: pf-proof

By the fundamental theorem of calculus and the chain rule,
$$
\begin{aligned}
f'(x)
&=2\frac{\sin(2x)}{2x}-\frac{\sin x}{x}\\
&=\frac{\sin 2x-\sin x}{x}.
\end{aligned}
$$
Using $\sin 2x=2\sin x\cos x$ gives the factored form.

:::

:::

::: {.pf-step #s1-2}

The critical points in $(0,3\pi/2)$ are
$$
x=\frac\pi3
\quad\text{and}\quad
x=\pi.
$$


::: pf-proof

Since $x>0$, step [](#s1-1){.pf-ref} shows that $f'(x)=0$ exactly when
$$
\sin x=0
\quad\text{or}\quad
\cos x=\frac12.
$$
In $(0,3\pi/2)$, the first equation gives $x=\pi$, and the second gives $x=\pi/3$.

:::

:::

::: {.pf-step #s1-3}

$f'$ changes sign from positive to negative at $x=\pi/3$, and from negative to positive at $x=\pi$.


::: pf-proof

The denominator in step [](#s1-1){.pf-ref} is positive on the interval. On $(0,\pi/3)$, both $\sin x$ and $2\cos x-1$ are positive, so $f'(x)>0$. On $(\pi/3,\pi)$, one has $\sin x>0$ and $2\cos x-1<0$, so $f'(x)<0$. On $(\pi,3\pi/2)$, both factors are negative, so $f'(x)>0$.

:::

:::

::: {.pf-step #s1-4}

The local maximum occurs at
$$
\boxed{x=\frac\pi3},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-3){.pf-ref}, $f'$ changes from positive to negative at $\pi/3$, so $f$ has a local maximum there. The other critical point, $\pi$, is a local minimum because the sign change there is from negative to positive.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies the requested local-maximum point and corresponding choice.

:::

:::

:::
