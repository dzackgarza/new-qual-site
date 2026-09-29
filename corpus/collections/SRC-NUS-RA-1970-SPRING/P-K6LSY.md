---
schema: qual/card@1
id: P-K6LSY
kind: problem
title: Finite interval covers versus Lebesgue outer measure, and Borel preimages under
  measurable functions
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove or disprove each of the following statements.

(f) If $E \subset \mathbb{R}$ and

    $\mu(E) = \inf\{\sum_{I_i \in S} |I_i| : S = \{I_i\}_{i=1}^n \text{ such that } E \subset \union_{i=1}^n I_i \text{ for some } n \in \mathbb{N}\}$

    then $\mu$ coincides with the outer measure of $E$.

(g) If $E$ is a Borel set and $f$ is a measurable function, then $f^{-1}(E)$ is also measurable.
:::

::: {.solution}

::: pf

::: {.pf-step #statement-f-false}
Statement (f) is false.

::: pf-proof

::: pf-step
Definition of $\mu(E)$ and Lebesgue outer measure $m^*(E)$:
For $E \subseteq \RR$,
$$
\mu(E) = \inf \left\{ \sum_{i=1}^n |I_i| : n \in \NN, E \subseteq \bigcup_{i=1}^n I_i, I_i \text{ open/closed/any bounded intervals} \right\},
$$
while the Lebesgue outer measure is:
$$
m^*(E) = \inf \left\{ \sum_{i=1}^\infty |I_i| : E \subseteq \bigcup_{i=1}^\infty I_i, I_i \text{ intervals} \right\}.
$$
:::

::: pf-step
Counterexample: Let $E = \mathbb{Q} \cap [0, 1]$.
:::

::: pf-step
$m^*(E) = 0$.

::: pf-proof
$E$ is countable, so as a countable set of real numbers, its Lebesgue outer measure is $m^*(E) = 0$.
:::

:::

::: pf-step
$\mu(E) = 1$.

::: pf-proof

::: pf-step
Let $\{I_1, \dots, I_n\}$ be any finite collection of open intervals such that $E \subseteq \bigcup_{i=1}^n I_i$.
:::

::: pf-step
Since $E = \mathbb Q \cap [0, 1]$ is dense in $[0, 1]$, the closure of $E$ is $\overline{E} = [0, 1]$.
:::

::: pf-step
Since $\bigcup_{i=1}^n \overline{I_i}$ is closed and contains $E$, it must contain $\overline{E} = [0, 1]$:
$$
[0, 1] \subseteq \bigcup_{i=1}^n \overline{I_i}.
$$
:::

::: pf-step
By subadditivity of the Lebesgue measure of intervals,
$$
1 = m([0, 1]) \leq m\left(\bigcup_{i=1}^n \overline{I_i}\right) \leq \sum_{i=1}^n m(\overline{I_i}) = \sum_{i=1}^n |I_i|.
$$
:::

::: pf-step
Taking the infimum over all finite covers gives $\mu(E) \geq 1$.
:::

::: pf-step
Since the single interval $I_1 = [0, 1]$ covers $E$ with length $|I_1| = 1$, we have $\mu(E) \leq 1$.
:::

::: pf-step
Thus $\mu(E) = 1$.
:::

:::

:::

::: pf-step
Since $\mu(E) = 1 \neq 0 = m^*(E)$, $\mu$ does not coincide with the outer measure of $E$. Hence statement (f) is false.
:::

:::

:::

::: {.pf-step #statement-g-true}
Statement (g) is true.

::: pf-proof

::: pf-step
Let $(\RR, \mathcal L, m)$ be the Lebesgue measure space and $(\RR, \mathcal B)$ be the Borel measurable space on $\RR$.
:::

::: {.pf-step #f-measurable-iff-open-preimages-in-L}
A function $f: \RR \to \RR$ is (Lebesgue) measurable if and only if for every open set $U \subseteq \RR$, $f^{-1}(U) \in \mathcal L$.

::: pf-proof
This is the definition of Lebesgue measurability of a real-valued function; it is equivalent to $f^{-1}((a, \infty)) \in \mathcal L$ for all $a \in \RR$.
:::

:::

::: pf-step
Define the family of sets $\mathcal S \definedas \{A \subseteq \RR : f^{-1}(A) \in \mathcal L\}$.
:::

::: pf-step
$\mathcal S$ is a $\sigma$-algebra on $\RR$.

::: pf-proof

::: pf-step
$\emptyset \in \mathcal S$ since $f^{-1}(\emptyset) = \emptyset \in \mathcal L$.
:::

::: pf-step
If $A \in \mathcal S$, then $f^{-1}(\RR \setminus A) = \RR \setminus f^{-1}(A) \in \mathcal L$ (since $\mathcal L$ is closed under complements), so $\RR \setminus A \in \mathcal S$.
:::

::: pf-step
If $\{A_n\}_{n=1}^\infty \subseteq \mathcal S$, then $f^{-1}\left(\bigcup_{n=1}^\infty A_n\right) = \bigcup_{n=1}^\infty f^{-1}(A_n) \in \mathcal L$ (since $\mathcal L$ is closed under countable unions), so $\bigcup_{n=1}^\infty A_n \in \mathcal S$.
:::

:::

:::

::: pf-step
$\mathcal S$ contains all open subsets of $\RR$.

::: pf-proof
By step [](#f-measurable-iff-open-preimages-in-L){.pf-ref}, for every open set $U \subseteq \RR$, $f^{-1}(U) \in \mathcal L$, so $U \in \mathcal S$.
:::

:::

::: pf-step
$\mathcal B \subseteq \mathcal S$.

::: pf-proof
The Borel $\sigma$-algebra $\mathcal B$ is by definition the smallest $\sigma$-algebra containing all open sets in $\RR$. Since $\mathcal S$ is a $\sigma$-algebra containing all open sets, $\mathcal B \subseteq \mathcal S$.
:::

:::

::: pf-step
For every Borel set $E \in \mathcal B$, $f^{-1}(E) \in \mathcal L$ (i.e. $f^{-1}(E)$ is Lebesgue measurable).

::: pf-proof
Since $E \in \mathcal B \subseteq \mathcal S$, by definition of $\mathcal S$ we have $f^{-1}(E) \in \mathcal L$.
:::

:::

:::

:::

::: pf-qed
Step [](#statement-f-false){.pf-ref} disproves (f) with $E = \mathbb Q \cap [0, 1]$, and step [](#statement-g-true){.pf-ref} proves (g).
:::

:::
