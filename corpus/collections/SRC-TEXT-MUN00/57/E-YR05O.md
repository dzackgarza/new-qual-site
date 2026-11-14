---
schema: qual/card@1
id: E-YR05O
kind: problem
title: Antipode-preserving maps of the circle act by odd powers
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 57 Exercise 3, printed p. 359,
    with Theorem 57.1 and the lifting theory of Section 54. The card lifts $h$ to $H:\RR\to\RR$ with $H(0)=0$; antipode preservation gives $H(t+\frac12)-H(t)\in\frac12+\ZZ$, which is constant by continuity, so $H(t+1)=H(t)+2m+1$ and the degree is odd. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof of the step the exercise needs has been located: Hatcher, *Algebraic
    Topology* (2002), the proof of Theorem 1.10, printed p. 33, held at
    tmp/sources/hatcher-2002-algebraic-topology.md. The solution transcribes that lifting
    computation: a loop with $\ell(s+\frac12)=-\ell(s)$ lifts to $\tilde\ell$ with
    $\tilde\ell(s+\frac12)=\tilde\ell(s)+\frac q2$ for one odd integer $q$, and $\tilde\ell(1)=q$.
    Hatcher's Theorem 1.10 is the Borsuk-Ulam theorem for $S^2$, and its loop is $g\eta$ with
    $\eta$ circling the equator; the exercise's $h$ is itself such a loop, and the card states
    that it applies the computation to that loop and does not use the book's hint (the map $k$ of
    the proof of Theorem 57.1 on printed pp. 356-357, with $q(z)=z^2$). Checked against the book:
    the exercise text on printed p. 359, Theorem 57.1 (printed pp. 356-357) for the hypothesis
    that $h$ is antipode-preserving, Theorem 53.1 (printed p. 337) for $p:\RR\to S^1$, Lemma 54.1
    (printed p. 342) for path lifting, and Theorem 54.5 (printed p. 345) for the lifting
    correspondence being an isomorphism onto $\ZZ$ with $\phi([p_0])=1$. Not claimed: that
    Hatcher states this exercise, or that his theorem covers $S^1$ -- it does not, and the
    identification $\ell=h\circ p_0$ is where the exercise meets his computation.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source and its
    page named in its own text and with the lifting correspondence of Theorem 54.5 used to convert
    $\tilde\ell(1)=q$ into $h_*(a)=a^q$. The earlier proof made the same computation for a lift
    $H$ of $h\circ p$ and concluded the same; it was removed because the card is to carry the
    published one.
---

::: {.exercise}

Let $h: S^1 \to S^1$ be continuous and antipode-preserving with $h(b_0) = b_0$.
Show that $h_*$ carries a generator of $\pi_1(S^1, b_0)$ to an odd power of itself.
[Hint: If $k$ is the map constructed in the proof of Theorem 57.1, show that $k_*$ does the same.]
:::

::: {.solution}
The exercise is §57 Exercise 3, printed p. 359. The proof is transcribed from
Hatcher, *Algebraic Topology* (2002), the proof of Theorem 1.10, printed p. 33:
the lifting step there takes a loop $h$ with $h(s+\frac12)=-h(s)$ and shows that
its lift $\tilde h$ satisfies $\tilde h(s+\frac12)=\tilde h(s)+\frac q2$ for a
single odd integer $q$, so that $\tilde h(1)=\tilde h(0)+q$ and the loop
represents an odd multiple of a generator. Hatcher states that computation for
a loop in $S^1$ that arises as $g\eta$ with $\eta$ circling the equator of
$S^2$, and uses it to prove the Borsuk--Ulam theorem; here it is applied to the
loop $\ell$ that $h$ itself is, which is all the exercise asks for. The book's
hint (use the map $k$ constructed in the proof of Theorem 57.1) reaches the
same conclusion through $q(z)=z^2$; the computation below does not need it.

Notation. Let $p:\RR\to S^1$ be the covering map $p(t)=e^{2\pi it}$ of Theorem
53.1 (printed p. 337), put $b_0=p(0)=1$, let $p_0=\restrictionof{p}{[0,1]}$, and let
$a=[p_0]\in\pi_1(S^1,b_0)$. By Theorem 54.5 (printed p. 345) with $e_0=0$ the
lifting correspondence $\phi:\pi_1(S^1,b_0)\to\ZZ$, which sends $[f]$ to the
endpoint $\tilde f(1)\in p^{-1}(b_0)=\ZZ$ of the lift of $f$ starting at $0$, is
an isomorphism of groups, and $\phi(a)=1$; so $a$ generates the infinite cyclic
group $\pi_1(S^1,b_0)$, and powers are written multiplicatively.

::: pf

::: {.pf-step #loop}
$\ell=h\circ p_0$ is a loop in $S^1$ at $b_0$, and $h_*(a)=[\ell]$.

::: pf-proof
Since $h(b_0)=b_0$, $\ell(0)=h(p_0(0))=h(b_0)=b_0=\ell(1)$. By the definition of
the induced homomorphism, $h_*(a)=h_*([p_0])=[h\circ p_0]=[\ell]$.
:::

:::

::: {.pf-step #antipode}
$\ell\big(s+\frac12\big)=-\ell(s)$ for every $s\in[0,\frac12]$.

::: pf-proof
For such $s$ the point $s+\frac12$ lies in $[0,1]$, and
$$
p_0\Big(s+\frac12\Big)=e^{2\pi i(s+1/2)}=e^{\pi i}e^{2\pi is}=-p_0(s).
$$
Because $h$ is antipode-preserving,
$$
\ell\Big(s+\frac12\Big)=h\big({-p_0(s)}\big)=-h\big(p_0(s)\big)=-\ell(s).
$$
:::

:::

::: {.pf-step #lift}
There is a path $\tilde\ell:I\to\RR$ with $p\circ\tilde\ell=\ell$ and
$\tilde\ell(0)=0$.

::: pf-proof
Apply the path-lifting lemma (Lemma 54.1, printed p. 342) to the covering map
$p$ and the path $\ell$ starting at $b_0=p(0)$; it gives a unique lift
$\tilde\ell$ of $\ell$ with $\tilde\ell(0)=0$.
:::

:::

::: {.pf-step #odd-increment}
There is an odd integer $q$ with
$\tilde\ell\big(s+\frac12\big)=\tilde\ell(s)+\frac q2$ for every
$s\in[0,\frac12]$.

::: pf-proof
Let $s\in[0,\frac12]$. By steps [](#antipode){.pf-ref} and
[](#lift){.pf-ref},
$$
p\Big(\tilde\ell\big(s+\tfrac12\big)\Big)=\ell\big(s+\tfrac12\big)=-\ell(s)=-p\big(\tilde\ell(s)\big)
=p\Big(\tilde\ell(s)+\tfrac12\Big),
$$
the last equality because $p(t+\frac12)=-p(t)$ for all $t$. Two reals have the
same image under $p$ exactly when they differ by an integer, so
$$
m(s)\coloneqq \tilde\ell\big(s+\tfrac12\big)-\tilde\ell(s)-\tfrac12\in\ZZ .
$$
The path $\tilde\ell$ is continuous, so $s\mapsto m(s)$ is a continuous
function on the connected interval $[0,\frac12]$ with values in $\ZZ$; hence it
is constant, say $m(s)=m$ for all $s$. Put $q=2m+1$, an odd integer. Then
$\tilde\ell(s+\frac12)=\tilde\ell(s)+\frac12+m=\tilde\ell(s)+\frac q2$.
:::

:::

::: {.pf-step}
$h_*(a)=a^{q}$ for the odd integer $q$ of step
[](#odd-increment){.pf-ref}.

::: pf-proof
Evaluating step [](#odd-increment){.pf-ref} at $s=0$ and at $s=\frac12$, and
using $\tilde\ell(0)=0$ from step [](#lift){.pf-ref},
$$
\tilde\ell(1)=\tilde\ell\big(\tfrac12\big)+\tfrac q2
=\tilde\ell(0)+\tfrac q2+\tfrac q2=q .
$$
By the definition of $\phi$, $\phi([\ell])=\tilde\ell(1)=q$, and $\phi$ is an
isomorphism with $\phi(a)=1$, so $[\ell]=a^{q}$; by step [](#loop){.pf-ref},
$h_*(a)=[\ell]=a^{q}$, which is an odd power of $a$ because $q=2m+1$. Since the
only generators of $\pi_1(S^1,b_0)$ are $a$ and $a^{-1}$, and
$h_*(a^{-1})=a^{-q}=(a^{-1})^{q}$ with $q$ again odd, $h_*$ carries every
generator to an odd power of itself.
:::

:::

:::
:::
