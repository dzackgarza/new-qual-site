---
schema: qual/card@1
id: E-5Q5LW
kind: exercise
title: Nonvanishing holomorphic functions of modulus one on the circle are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Schwarz Reflection
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose $f$ is continuous and nonvanishing on $\bar \DD$, and holomorphic in $\DD$.
Prove that if $\abs{z} = 1 \implies \abs{f(z)} = 1$, then $f$ is constant.

> Hint: Extend $f$ to all of $\CC$ by $f(z) = 1/ \bar{f(1/\bar z)}$ for any $\abs{z} > 1$, and argue as in the Schwarz reflection principle.
:::

::: {.solution}
First, note that the Schwarz reflection principle can be applied here: let $T: \DD\to \HH$ be the Cayley map, and consider $\tilde f \da T\circ f \circ T\inv: \HH\to \HH$.
Now $T(S^1) = \RR$, and since $f(z)\in S^1$ when $z\in S^1$, we have $\tilde f(\RR) = \RR$, i.e. this is a real-valued function on $\RR$.
So $\tilde f$ extends holomorphically to $\tilde F:\CC\to CC$, and we can pull this back to a holomorphic extension of $f$.

Extend $f$ to $F:\CC\to \CC$ by $f(z) = 1/\bar{f(1/\bar{z})}$ for $z\in \DD^c$, which generally has poles at the points $1/\bar{z_k}$ for $z_k\in \DD$ zeros of $f$.
Since $f$ is nonvanishing, $F$ has no poles and thus defines an entire function.
By definition of $F$, we have $F(\CC) \subseteq f\qty{\ts{\abs{z} \leq 1}} \union \bar{ f\qty{\ts{\abs{z} \geq 1}}}$, which are both the continuous images of compact sets and thus compact and bounded.
So $F$ is a bounded entire function and thus constant.
:::
