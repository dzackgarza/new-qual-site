---
schema: qual/card@1
id: P-BKS19-5A
kind: problem
title: Roots of $e^z=3z^6$ in the upper half of the unit disk
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 Rouché argument. The answer is correct; the solution below replaces the source's graphical assertion about real roots by a monotonicity proof and verifies that the six roots in the disk are simple.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the strict Rouché inequality on the unit circle, the two real roots by logarithmic monotonicity, simplicity of roots in the disk, and conjugate pairing.
---

::: {.problem}
Find the number of complex roots of
$$
e^z=3z^6
$$
with $\abs{z}<1$ that have positive imaginary part.
:::

::: {.solution}

Set
$$
F(z)\coloneqq e^z-3z^6.
$$

::: pf

::: {.pf-step #s1-1}

The function $F$ has six zeros in $\abs{z}<1$, counted with multiplicity.


::: pf-proof

On $\abs{z}=1$,
$$
\abs{e^z}=e^{\operatorname{Re}z}\leq e<3=\abs{3z^6}.
$$
Hence Rouché's theorem applied to $3z^6$ and $-e^z$ shows that
$$
3z^6-e^z=-F(z)
$$
has the same number of zeros in the unit disk as $3z^6$, namely six, counted with multiplicity.

:::

:::

::: {.pf-step #s1-2}

Exactly one real zero of $F$ lies in $(-1,0)$ and exactly one lies in $(0,1)$.


::: pf-proof

For real $x\neq0$, the equation $F(x)=0$ is equivalent to
$$
\Phi(x)\coloneqq x-\log3-6\log\abs{x}=0.
$$
On $(-1,0)$,
$$
\Phi'(x)=1-\frac6x>0,
$$
while
$$
\Phi(-1)=-1-\log3<0,
\qquad
\lim_{x\to0^-}\Phi(x)=+\infty.
$$
Thus the intermediate value theorem and strict monotonicity give exactly one zero in $(-1,0)$.

On $(0,1)$ one has $\Phi'(x)=1-6/x<0$, together with
$$
\lim_{x\to0^+}\Phi(x)=+\infty,
\qquad
\Phi(1)=1-\log3<0,
$$
because $3>e$. Hence there is exactly one zero in $(0,1)$.

:::

:::

::: {.pf-step #s1-3}

Every zero of $F$ in the unit disk is simple.


::: pf-proof

If $z$ were a multiple zero, then $F(z)=F'(z)=0$. Since
$$
F'(z)=e^z-18z^5,
$$
the two equations would give
$$
3z^6=e^z=18z^5.
$$
The number $z$ cannot be $0$, so division by $3z^5$ gives $z=6$, which is outside the unit disk. Thus no zero in the disk is multiple.

:::

:::

::: {.pf-step #s1-4}

Exactly four zeros in the unit disk are nonreal, and exactly two of them have positive imaginary part.


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} there are six distinct zeros in the disk. Step [](#s1-2){.pf-ref} accounts for exactly two real zeros, leaving four nonreal zeros. Since
$$
F(\overline z)=\overline{F(z)},
$$
nonreal zeros occur in conjugate pairs. In each conjugate pair exactly one zero has positive imaginary part. Therefore exactly two of the four nonreal zeros lie in the upper half-plane.

:::

:::

::: {.pf-step #s1-5}

The requested number is
$$
\boxed{2}.
$$


::: pf-proof

This is the conclusion of step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested count.

:::

:::

:::
