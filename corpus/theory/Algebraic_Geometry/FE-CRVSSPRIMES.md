---
schema: qual/card@1
id: FE-CRVSSPRIMES
kind: example
title: Fixing the curve and varying $p$, and the density of supersingular primes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Characteristic p
  - Complex Multiplication
relations:
- kind: uses
  target: T-CRVHASSE
- kind: uses
  target: T-CRVCM
- kind: related-to
  target: T-CRVCMCFT
review: draft
prompts:
- Fix an elliptic curve over $\QQ$ and reduce it mod $p$ --- for how many $p$ is the reduction supersingular?
- Work out the supersingular primes of $y^2 = x^3 - x$ by hand.
- How does complex multiplication change the answer?
- Given a curve over $\QQ$, what cheap test rules out complex multiplication?
---

::: {.example title="The setup"}
Let $X = V(f) \subseteq \PP^2_{/\ZZ}$ with $f \in \ZZ[x,y,z]$ a cubic whose base change to $\CC$ is smooth.
For all but finitely many primes the reduction $X_{(p)} \subseteq \PP^2_{/\FF_p}$ is again smooth, and one can ask for
\[
B \da \ts{ p \st X_{(p)} \text{ is smooth over } \bar\FF_p \text{ and has Hasse invariant } 0 } .
\]
The answer depends entirely on whether $X_{/\CC}$ has complex multiplication:

- **With CM** by an order in $K$: for $p$ of good reduction, $p \in B$ exactly when $p$ does not split in $K$, that is when $p$ is inert or ramified.
  Half the primes split, so $B$ has density $\tfrac{1}{2}$.
  This is Deuring's theorem.

- **Without CM**: $B$ has density $0$, and $B$ is nevertheless infinite.
  Both of these are theorems, the second Elkies'.
  A finer count is not known: the expected asymptotic $\abs{\ts{p \in B \st p \leq x}} \sim c\,\tfrac{\sqrt x}{\log x}$ is the Lang--Trotter conjecture and is open.
:::

::: {.remark title="What is proved and what is not"}
State the three claims separately, because they have different status and an examiner may push on exactly that.
Deuring's criterion is a clean equivalence and gives the density $\tfrac12$ immediately from Chebotarev, or from Dirichlet in the cases where the splitting condition is a congruence.
Density zero in the non-CM case follows from the distribution of Frobenius traces.
Infinitude in the non-CM case is much harder and was open for a long time; it is a theorem only for elliptic curves over $\QQ$.
The $\sqrt x/\log x$ growth is a conjecture and should be labelled as one.
:::

::: {.example title="$y^2 = x^3 - x$, worked out"}
Here $\lambda = -1$, $j = 1728$, and the curve has CM by $\ZZ[i]$.
Apply the criterion directly: with $m = \tfrac{p-1}{2}$ and $g(x) = x(x^2-1)$,
\[
g(x)^m = x^m (x^2-1)^m ,
\]
so the coefficient of $x^{p-1} = x^{2m}$ is the coefficient of $x^m$ in $(x^2-1)^m$.
Only even powers appear there, so that coefficient is $0$ when $m$ is odd, and $(-1)^{m/2}\binom{m}{m/2}$ when $m$ is even --- which is prime to $p$, since $m < p$.
Hence
\[
X_{(p)} \text{ supersingular}
\iff m = \tfrac{p-1}{2} \text{ is odd}
\iff p \equiv 3 \bmod 4 .
\]
And $p \equiv 3 \bmod 4$ is exactly the condition that $p$ stays prime in $\ZZ[i]$, matching the general statement.
By Dirichlet these have density $\tfrac{1}{2}$ and there are infinitely many.
:::

::: {.example title="$y^2 = x(x-1)(x-3)$, the contrast"}
Here $\lambda = 3$ and
\[
j = 2^8 \cdot \frac{(9-3+1)^3}{9 \cdot 4} = \frac{2^6 \cdot 7^3}{3^2} \notin \ZZ .
\]
Computing $h_p(3) \bmod p$ for the primes of good reduction, the only supersingular prime below $120$ is $p = 23$ --- sparse enough to guess density zero, and that guess is right, because a non-integral $j$ rules out complex multiplication by any order at all, let alone one of class number one.
:::

::: {.remark}
The mechanism behind the density $\tfrac{1}{2}$ is worth naming, because it explains why the two cases look so different.
For a CM curve the reduction inherits the CM order, and the splitting behaviour of $p$ in $K$ decides whether the reduced endomorphism ring stays commutative.
When $p$ splits, Frobenius generates the old imaginary quadratic order and the curve is ordinary; when $p$ is inert or ramified it cannot, the endomorphism ring jumps to a quaternion order, and the curve is supersingular.
So a single congruence condition governs every $p$ at once.

Without CM there is no such rigid structure and the supersingular primes are governed instead by how often the Frobenius trace $a_p$ vanishes, a much thinner condition; density zero, infinitude, and the $\sqrt x / \log x$ heuristic all belong to that side.

The practical use for exams runs in the other direction.
$j \notin \ZZ$ is a one-line proof that a curve has no CM by a class-number-one order, and $j$ not an algebraic integer rules out CM entirely.
This is the cheapest available route, and the reason to state the class field theory theorem at all when the question looks purely characteristic-$p$.
:::
