---
schema: qual/card@1
id: P-MAXAT-6-03
kind: problem
title: Maxim algebraic topology 6.3
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 3 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Study possible immersions (embeddings) of $\mathbb { R P } ^ { n }$ into $\RR ^ { n + k }$ . (Hint: use S-W classes)
:::

::: {.solution}

The Stiefel--Whitney classes give a necessary lower bound on the codimension $k$. Let
\[
a\in H^1(\RP^n;\FF_2)
\]
be the standard generator.

::: pf

::: {.pf-step #s1-1}

The tangent bundle satisfies
\[
w(T\RP^n)=(1+a)^{n+1}.
\]


::: pf-proof

The standard stable isomorphism
\[
T\RP^n\oplus\varepsilon^1
\cong(n+1)\gamma^1
\]
and $w(\gamma^1)=1+a$ give the formula by the Whitney product theorem.

:::

:::

::: {.pf-step #s1-2}

If
\[
f:\RP^n\looparrowright\RR^{n+k}
\]
is a smooth immersion with normal bundle $\nu$ of rank $k$, then
\[
T\RP^n\oplus\nu\cong\varepsilon^{n+k}.
\]


::: pf-proof

The derivative identifies $T\RP^n$ with a rank-$n$ subbundle of the pulled-back tangent bundle
\[
f^*T\RR^{n+k}\cong\varepsilon^{n+k}.
\]
Choosing the orthogonal complement gives the rank-$k$ normal bundle $\nu$ and the displayed splitting.

:::

:::

::: {.pf-step #s1-3}

Consequently the total Stiefel--Whitney class of the normal bundle is
\[
w(\nu)=(1+a)^{-(n+1)}
=\sum_{j\geq0}\binom{n+j}{j}a^j
\quad\text{in }\FF_2[a]/(a^{n+1}).
\]


::: pf-proof

Whitney multiplicativity applied to step [](#s1-2){.pf-ref} gives
\[
w(T\RP^n)w(\nu)=1.
\]
Use step [](#s1-1){.pf-ref} and the formal binomial expansion
\[
(1+a)^{-m}=\sum_{j\geq0}(-1)^j\binom{m+j-1}{j}a^j.
\]
Over $\FF_2$ the signs disappear, and setting $m=n+1$ yields the stated coefficients.

:::

:::

::: {.pf-step #s1-4}

Since $\nu$ has rank $k$,
\[
w_j(\nu)=0
\qquad(j>k).
\]
Therefore an immersion can exist only if
\[
\binom{n+j}{j}\equiv0\pmod2
\qquad\text{for every }k<j\leq n.
\]


::: pf-proof

Stiefel--Whitney classes above the rank of a vector bundle vanish. By step [](#s1-3){.pf-ref},
\[
w_j(\nu)=\binom{n+j}{j}a^j.
\]
For $j\leq n$, the class $a^j$ is nonzero in $H^j(\RP^n;\FF_2)$. Hence vanishing is equivalent to evenness of the binomial coefficient.

:::

:::

::: {.pf-step #s1-5}

Let $2^s$ be the least power of two strictly larger than $n$. Then
\[
w_{,2^s-n-1}(\nu)=a^{,2^s-n-1}\ne0.
\]


::: pf-proof

Put
\[
j=2^s-n-1.
\]
Then $1\leq j\leq n$ whenever $2^{s-1}\leq n<2^s$ and $n\ne2^s-1$; in the endpoint case $j=0$ gives no obstruction. The coefficient in step [](#s1-3){.pf-ref} is
\[
\binom{n+j}{j}
=\binom{2^s-1}{j}.
\]
Every binomial coefficient in row $2^s-1$ is odd: modulo $2$,
\[
(1+t)^{2^s-1}=1+t+t^2+\cdots+t^{2^s-1}.
\]
Thus the coefficient is $1$ mod $2$, proving the claim.

:::

:::

::: {.pf-step #s1-6}

Hence, whenever $n\ne2^s-1$, every immersion
\[
\RP^n\looparrowright\RR^{n+k}
\]
must satisfy
\[
\boxed{k\geq2^s-n-1.}
\]


::: pf-proof

The nonzero class in step [](#s1-5){.pf-ref} is a Stiefel--Whitney class of the rank-$k$ normal bundle. Its degree cannot exceed $k$, giving the inequality.

:::

:::

::: {.pf-step #s1-7}

More sharply, the complete Stiefel--Whitney obstruction is
\[
\boxed{
k\geq
\max\{j\leq n:\binom{n+j}{j}\text{ is odd}\}.}
\]


::: pf-proof

Step [](#s1-4){.pf-ref} says every nonzero inverse Stiefel--Whitney class must occur in degree at most the normal rank. Taking the largest degree with odd coefficient gives exactly this necessary bound. Lucas's theorem can be used to read the odd coefficients directly from the binary expansion of $n$.

:::

:::

::: {.pf-step #s1-8}

The same bound applies to embeddings
\[
\RP^n\hookrightarrow\RR^{n+k}.
\]


::: pf-proof

Every smooth embedding is in particular a smooth immersion, and its geometric normal bundle satisfies the same stable tangent-normal identity of step [](#s1-2){.pf-ref}. Hence every Stiefel--Whitney obstruction derived above remains necessary.

:::

:::

::: pf-step

These characteristic classes provide obstructions, not a general sufficiency theorem.


::: pf-proof

Vanishing of the inverse Stiefel--Whitney classes above degree $k$ is necessary for a rank-$k$ stable normal bundle, but Stiefel--Whitney classes do not classify normal bundles or remove all immersion/embedding obstructions. Thus the conclusions above are precisely the restrictions supplied by the hint, rather than an unsupported claim that every remaining codimension occurs.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} through [](#s1-8){.pf-ref} give the requested Stiefel--Whitney analysis of possible immersion and embedding codimensions.

:::

:::

:::
