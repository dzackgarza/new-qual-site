---
schema: qual/card@1
id: P-UCLAB04S-09
kind: problem
title: Equivalent characterizations of a finite-dimensional isometry
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Exam Spring 2004 PDF.
---

::: {.problem}
Let $V$ be a finite-dimensional real inner product space with inner product $(\ ,\ )$, and let $T:V\to V$ be linear.
Show that the following are equivalent:

(a) $(Tx,Ty)=(x,y)$ for all $x,y\in V$;

(b) $\|T(x)\|=\|x\|$ for all $x\in V$;

(c) $T^*T=\operatorname{Id}_V$, where $T^*$ is the adjoint of $T$;

(d) $TT^*=\operatorname{Id}_V$.
:::

::: {.solution}
<1>1. Condition (a) implies condition (b).

::: {.proof}
Assume
\[
(Tx,Ty)=(x,y)
\]
for all $x,y\in V$.
Taking $y=x$ gives
\[
\|Tx\|^2
=(Tx,Tx)
=(x,x)
=\|x\|^2.
\]
Both norms are nonnegative, so
\[
\|Tx\|=\|x\|.
\]
:::

<1>2. Condition (b) implies condition (a).

::: {.proof}
Assume
\[
\|Tx\|=\|x\|
\]
for every $x\in V$.
Using the real polarization identity,
\[
(u,v)
=
\frac12
\left(
\|u+v\|^2-\|u\|^2-\|v\|^2
\right).
\]
Therefore
\[
\begin{aligned}
(Tx,Ty)
&=
\frac12
\left(
\|T(x+y)\|^2-\|Tx\|^2-\|Ty\|^2
\right)\\
&=
\frac12
\left(
\|x+y\|^2-\|x\|^2-\|y\|^2
\right)\\
&=
(x,y).
\end{aligned}
\]
Thus (a) holds.
:::

<1>3. Condition (a) implies condition (c).

::: {.proof}
Assume (a).
For all $x,y\in V$,
\[
(T^*Tx,y)
=(Tx,Ty)
=(x,y).
\]
Hence
\[
((T^*T-I)x,y)=0
\]
for every $y\in V$.
Taking
\[
y=(T^*T-I)x
\]
gives
\[
\|(T^*T-I)x\|^2=0.
\]
Thus
\[
T^*Tx=x
\]
for every $x$, so
\[
\boxed{T^*T=I}.
\]
:::

<1>4. Condition (c) implies condition (b).

::: {.proof}
Assume
\[
T^*T=I.
\]
Then for every $x$,
\[
\begin{aligned}
\|Tx\|^2
&=
(Tx,Tx)\\
&=
(T^*Tx,x)\\
&=
(x,x)\\
&=
\|x\|^2.
\end{aligned}
\]
Taking square roots gives
\[
\|Tx\|=\|x\|.
\]
:::

<1>5. Condition (c) implies that $T$ is injective.

::: {.proof}
If
\[
Tx=0,
\]
then
\[
x
=
T^*Tx
=0.
\]
Thus
\[
\ker T=\{0\}.
\]
:::

<1>6. Because $V$ is finite-dimensional, condition (c) implies that $T$ is invertible and
\[
T^{-1}=T^*.
\]

::: {.proof}
By step <1>5, $T$ is injective.
For an endomorphism of a finite-dimensional vector space, injectivity implies surjectivity, hence invertibility.
From
\[
T^*T=I,
\]
multiply on the right by $T^{-1}$ to obtain
\[
T^*=T^{-1}.
\]
:::

<1>7. Condition (c) implies condition (d).

::: {.proof}
By step <1>6,
\[
T^*=T^{-1}.
\]
Therefore
\[
TT^*
=
TT^{-1}
=I.
\]
:::

<1>8. Condition (d) implies condition (c).

::: {.proof}
Assume
\[
TT^*=I.
\]
Then $T^*$ is injective, hence surjective because $V$ is finite-dimensional.
Thus $T^*$ is invertible.
From
\[
TT^*=I,
\]
one gets
\[
T=(T^*)^{-1}.
\]
Therefore
\[
T^*T
=
T^*(T^*)^{-1}
=I.
\]
:::

<1>9. Hence conditions (a), (b), (c), and (d) are equivalent.

::: {.proof}
Steps <1>1--<1>4 prove
\[
(a)\iff(b)\iff(c),
\]
and steps <1>7--<1>8 prove
\[
(c)\iff(d).
\]
Therefore all four conditions are equivalent.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required equivalence.
:::
:::
