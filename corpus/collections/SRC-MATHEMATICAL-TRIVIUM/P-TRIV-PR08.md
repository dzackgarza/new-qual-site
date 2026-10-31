---
schema: qual/card@1
id: P-TRIV-PR08
kind: problem
title: Reliability of a five-relay bridge circuit
classification:
  areas: [prelim]
  topics:
  - Independence of Events
  - Conditional Probability
  - Bayes' Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The relay network is specified by Figure 7. Flash preserves only an image placeholder/caption, so the circuit topology needed to solve the probability problem is unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the missing-figure note with a description of the Figure 7 bridge circuit from Probability Problem 8 on page 27 of the source PDF.
---

::: {.problem}
Consider the circuit shown in figure.
Each of its five relays is closed with the probability $p$ independently of other relays.

(a) Find the probability that a signal will pass through the circuit.

(b) Find the probability that the relay $E$ is open if it is known that the signal has passed through the circuit.

Figure 7 of the source (the circuit) is a bridge: from the input the line splits into an upper branch through relay $A$ to an upper node and a lower branch through relay $C$ to a lower node; the upper node is joined to the output through relay $B$, the lower node is joined to the output through relay $D$, and relay $E$ joins the upper node to the lower node.
:::

::: {.solution}

Let $S$ be the event that a signal passes from input to output.

::: pf

::: {.pf-step #s1-1}

Conditional on $E$ being open, the circuit consists of the two parallel series paths $AB$ and $CD$, so
$$
P(S\mid E\text{ open})=1-(1-p^2)^2=2p^2-p^4.
$$


::: pf-proof

With $E$ open, passage occurs exactly when $A$ and $B$ are both closed or $C$ and $D$ are both closed. The two path events depend on disjoint relays and are independent, each with probability $p^2$. Taking the complement gives the formula.

:::

:::

::: {.pf-step #s1-2}

Conditional on $E$ being closed, passage occurs exactly when at least one of $A,C$ is closed and at least one of $B,D$ is closed, so
$$
P(S\mid E\text{ closed})=(2p-p^2)^2.
$$


::: pf-proof

When $E$ is closed, the two intermediate nodes are connected and behave as one node. The probability that at least one of $A,C$ is closed is $1-(1-p)^2=2p-p^2$, and the same holds independently for $B,D$. Thus
$$
P(S\mid E\text{ closed})
=\bigl(1-(1-p)^2\bigr)^2
=(2p-p^2)^2.
$$
This direct characterization subsumes the failure cases described in the claim.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
P(S)=(1-p)(2p^2-p^4)+p(2p-p^2)^2.
$$


::: pf-proof

Use the law of total probability, with $P(E\text{ open})=1-p$ and $P(E\text{ closed})=p$, and substitute steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Simplifying gives
$$
\boxed{P(S)=2p^2+2p^3-5p^4+2p^5}.
$$


::: pf-proof

Expand step [](#s1-3){.pf-ref}:
$$
(1-p)(2p^2-p^4)+p(4p^2-4p^3+p^4)
=2p^2+2p^3-5p^4+2p^5.
$$

:::

:::

::: {.pf-step #s1-5}

The joint probability that $E$ is open and the signal passes is
$$
P(E\text{ open}\cap S)=(1-p)(2p^2-p^4).
$$


::: pf-proof

Multiply $P(E\text{ open})=1-p$ by the conditional probability in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
P(E\text{ open}\mid S)
=\frac{(1-p)(2p^2-p^4)}{2p^2+2p^3-5p^4+2p^5}}
$$
for $p>0$.


::: pf-proof

By the definition of conditional probability,
$$
P(E\text{ open}\mid S)=\frac{P(E\text{ open}\cap S)}{P(S)}.
$$
Substitute steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers part (a), and step [](#s1-6){.pf-ref} answers part (b).

:::

:::

:::
