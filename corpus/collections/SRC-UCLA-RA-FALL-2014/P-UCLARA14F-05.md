---
schema: qual/card@1
id: P-UCLARA14F-05
kind: problem
title: Density of a pushforward under a nonsingular continuous map
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 5 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $\phi : [0,1] \to [0,1]$ be continuous and let $d\mu$ be a Borel probability measure on $[0,1]$. Suppose $\mu(\phi^{-1}(E)) = 0$ for every Borel set $E \subseteq [0,1]$ with $\mu(E) = 0$. Show that there is a Borel measurable function $w : [0,1] \to [0,\infty)$ so that
$$
\int f \circ \phi(x)\,d\mu(x) = \int f(y) w(y)\,d\mu(y)
$$
for all continuous $f : [0,1] \to \RR$.
:::

::: {.solution}

::: pf

::: pf-step

Define a Borel measure $\nu$ on $[0,1]$ by
$$
\nu(E)=\mu(\phi^{-1}(E))
$$
for every Borel set $E\subseteq[0,1]$.


::: pf-proof

Since $\phi$ is continuous, it is Borel measurable, so
$$
\phi^{-1}(E)
$$
is Borel whenever $E$ is Borel. Thus $\nu$ is the pushforward measure
$$
\nu=\phi_*\mu.
$$
Because $\mu$ is a probability measure,
$$
\nu([0,1])
=
\mu(\phi^{-1}([0,1]))
=
\mu([0,1])
=1.
$$
Hence $\nu$ is a finite positive Borel measure.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{\nu\ll\mu}.
$$


::: pf-proof

If $E$ is Borel and
$$
\mu(E)=0,
$$
then the hypothesis gives
$$
\nu(E)
=
\mu(\phi^{-1}(E))
=0.
$$
This is exactly absolute continuity of $\nu$ with respect to $\mu$.

:::

:::

::: {.pf-step #s1-3}

There exists a Borel measurable function
$$
\boxed{
w:[0,1]\to[0,\infty)
}
$$
such that
$$
\nu(E)=\int_E w\,d\mu
$$
for every Borel set $E$.


::: pf-proof

The measures $\mu$ and $\nu$ are finite, hence $\sigma$-finite, and step
[](#s1-2){.pf-ref} gives $\nu\ll\mu$. The Radon--Nikodym theorem therefore yields a
measurable function
$$
w=\frac{d\nu}{d\mu}
$$
with
$$
\nu(E)=\int_Ew\,d\mu.
$$
Since $\nu$ is positive, the derivative may be chosen nonnegative
$\mu$-almost everywhere; changing it on a null set if necessary gives a
Borel representative with values in $[0,\infty)$.

:::

:::

::: {.pf-step #s1-4}

For every bounded Borel function $f:[0,1]\to\RR$,
$$
\int_{[0,1]} f(y)\,d\nu(y)
=
\int_{[0,1]} f(\phi(x))\,d\mu(x).
$$


::: pf-proof

For indicator functions
$$
f=\chi_E,
$$
the equality is precisely the definition
$$
\nu(E)=\mu(\phi^{-1}(E)).
$$
By linearity it holds for simple functions, and by monotone convergence it
extends to nonnegative Borel functions. Applying the result to positive and
negative parts gives the bounded real-valued case.

:::

:::

::: {.pf-step #s1-5}

For every continuous $f:[0,1]\to\RR$,
$$
\boxed{
\int f\circ\phi(x)\,d\mu(x)
=
\int f(y)w(y)\,d\mu(y)}.
$$


::: pf-proof

Every continuous function on compact $[0,1]$ is bounded and Borel measurable.
By step [](#s1-4){.pf-ref},
$$
\int f\circ\phi\,d\mu
=
\int f\,d\nu.
$$
By step [](#s1-3){.pf-ref},
$$
\int f\,d\nu
=
\int fw\,d\mu.
$$
Combining the two identities gives the claimed formula.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required representation.

:::

:::

:::
