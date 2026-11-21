---
schema: qual/card@1
id: E-SS5.EX-10
kind: problem
title: Hadamard products of $e^z-1$ and $\cos\pi z$
classification:
  areas:
  - complex-analysis
  topics:
  - Hadamard Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card carried two solution blocks: the answer, and a separate block holding only the provenance
    note that no retained solution set covers the exercise. Both rendered as solutions, so the page showed
    the exercise answered twice, the second time with a disclaimer. The note was moved to the head of the
    single solution block, where the corpus puts it on comparable cards; its wording and the answer were
    not changed.

---

::: {.exercise}
Find the Hadamard products for:

(a) $e^z - 1$.

(b) $\cos\pi z$.

[Hint: The answers are $e^{z/2} z \prod_{n=1}^{\infty} (1 + z^2/4n^2\pi^2)$ and $\prod_{n=0}^{\infty} (1 - 4z^2/(2n + 1)^2)$, respectively.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. The one input is Euler's product
$$
\frac{\sin\pi w}{\pi w}=\prod_{n\ge1}\Bigl(1-\frac{w^2}{n^2}\Bigr),
\tag{1}
$$
valid for all $w\in\CC$, which is the Hadamard factorisation of $\sin\pi w/(\pi w)$.

::: pf

::: {.pf-step #sine}
(1) holds as an identity of entire functions.

::: pf-proof
Both sides are entire: the left side because sine is entire, and the right side because the product converges normally, $\sum_n\abs{w^2/n^2}$ converging on every disc. Both vanish exactly at the nonzero integers and simply there, since $1-w^2/n^2$ has simple zeros at $w=\pm n$. Hadamard's factorisation theorem applied to the order-$1$ function $\sin\pi w/(\pi w)$, whose zeros are $\pm1,\pm2,\dots$ with genus $1$ elementary factors $(1-w/n)e^{w/n}(1+w/n)e^{-w/n}=1-w^2/n^2$, gives
$$
\frac{\sin\pi w}{\pi w}=e^{a+bw}\prod_{n\ge1}\Bigl(1-\frac{w^2}{n^2}\Bigr)
$$
for constants $a,b$. Setting $w=0$ gives $1=e^{a}\cdot1$, so $a=0$. Both sides of the resulting identity are even functions of $w$: the left side is even, and every factor $1-w^2/n^2$ is even. Hence $e^{bw}$ is even, which forces $b=0$ — otherwise $e^{bw}$ would take distinct values at $w$ and $-w$. So the exponential factor is $1$ and the identity holds.
:::

:::

::: {.pf-step #a}
(a) $e^z-1=e^{z/2}z\displaystyle\prod_{n\ge1}\Bigl(1+\frac{z^2}{4\pi^2n^2}\Bigr)$.

::: pf-proof
First $e^z-1=e^{z/2}\bigl(e^{z/2}-e^{-z/2}\bigr)=2e^{z/2}\sinh\dfrac z2$. Substitute $w=\dfrac{z}{2\pi i}$ in (1). Then $w^2=\dfrac{z^2}{4\pi^2i^2}=-\dfrac{z^2}{4\pi^2}$, so $1-\dfrac{w^2}{n^2}=1+\dfrac{z^2}{4\pi^2n^2}$, and $\pi w=\dfrac{z}{2i}$ with $\sin\dfrac{z}{2i}=\sin\Bigl(-\dfrac{iz}{2}\Bigr)=-\sin\dfrac{iz}{2}=-i\sinh\dfrac z2$. Hence the left side of (1) becomes $\dfrac{-i\sinh(z/2)}{z/(2i)}=\dfrac{2\sinh(z/2)}{z}$, so
$$
\frac{2\sinh(z/2)}{z}=\prod_{n\ge1}\Bigl(1+\frac{z^2}{4\pi^2n^2}\Bigr).
$$
Multiplying by $e^{z/2}z$ turns the left side into $2e^{z/2}\sinh(z/2)=e^z-1$, giving the display.
:::

:::

::: {.pf-step #b}
(b) $\cos\pi z=\displaystyle\prod_{n\ge0}\Bigl(1-\frac{4z^2}{(2n+1)^2}\Bigr)$.

::: pf-proof
From $\sin2\pi z=2\sin\pi z\cos\pi z$ we get $\cos\pi z=\dfrac{\sin2\pi z}{2\sin\pi z}$. Apply (1) twice: $\sin2\pi z=2\pi z\prod_{n\ge1}\bigl(1-\frac{4z^2}{n^2}\bigr)$ and $\sin\pi z=\pi z\prod_{n\ge1}\bigl(1-\frac{z^2}{n^2}\bigr)$, so
$$
\cos\pi z=\frac{\prod_{n\ge1}(1-4z^2/n^2)}{\prod_{n\ge1}(1-z^2/n^2)},
$$
the common factor $2\pi z$ cancelling. Split the numerator into even and odd indices: for $n=2m$ the factor is $1-\frac{4z^2}{4m^2}=1-\frac{z^2}{m^2}$, which cancels the denominator factor of index $m$; the surviving factors are those with $n=2m+1$, namely $1-\frac{4z^2}{(2m+1)^2}$. So the display holds, the quotient being legitimate because both products converge normally and neither vanishes at $z=0$.
:::

:::

::: {.pf-step}
The Hadamard products are $e^{z/2}z\prod_{n\ge1}\bigl(1+\frac{z^2}{4\pi^2n^2}\bigr)$ for $e^z-1$ and $\prod_{n\ge0}\bigl(1-\frac{4z^2}{(2n+1)^2}\bigr)$ for $\cos\pi z$.

::: pf-proof
Steps [](#a){.pf-ref} and [](#b){.pf-ref} give the two factorisations, which answer the exercise and agree with the answers stated in its hint. In each case the factors are attached to the zeros: the zeros of $e^z-1$ are $2\pi in$ for $n\in\ZZ$, and those of $\cos\pi z$ are the half-integers $(2n+1)/2$.
:::

:::

:::

We use the canonical product
$$
\frac{\sin \pi w}{\pi w}
=\prod_{n=1}^{\infty}\left(1-\frac{w^2}{n^2}\right).
\tag{1}
$$

For (a), put $w=z/(2\pi i)$ in (1). Since
$$
\sin\!\left(\frac z{2i}\right)=-i\sinh\frac z2,
$$
we obtain
$$
\frac{\sinh(z/2)}{z/2}
=\prod_{n=1}^{\infty}
\left(1+\frac{z^2}{4\pi^2n^2}\right).
$$
Using
$$
e^z-1=2e^{z/2}\sinh(z/2),
$$
we get
$$
\boxed{
e^z-1
=e^{z/2}z\prod_{n=1}^{\infty}
\left(1+\frac{z^2}{4\pi^2n^2}\right)}.
$$

For (b), use
$$
\cos\pi z=\frac{\sin 2\pi z}{2\sin\pi z}.
$$
Applying (1) to numerator and denominator gives
$$
\cos\pi z
=\frac{2\pi z\prod_{n\ge1}(1-4z^2/n^2)}
{2\pi z\prod_{n\ge1}(1-z^2/n^2)}.
$$
The factors indexed by even $n$ in the numerator cancel the denominator factors, leaving exactly the odd indices:
$$
\boxed{
\cos\pi z
=\prod_{n=0}^{\infty}
\left(1-\frac{4z^2}{(2n+1)^2}\right)}.
$$
These are the required Hadamard products.
:::

