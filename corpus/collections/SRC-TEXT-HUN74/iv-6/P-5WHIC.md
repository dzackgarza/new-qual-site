---
schema: qual/card@1
id: P-5WHIC
kind: problem
title: Multiplication and annihilator submodules of a cyclic PID module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Torsion
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Restored the omitted hypothesis that $R$ is a PID from an independent assignment explicitly reproducing Hungerford IV.6.3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section IV.6,
    exercise 3, book page 226, read from the page image: "Let A be a cyclic
    R-module of order r ∈ R. (a) If s ∈ R is relatively prime to r, then sA = A
    and A[s] = 0. (b) If s divides r, say sk = r, then sA ≅ R/(k) and
    A[s] ≅ R/(s)." The card states both parts, with the section's standing
    hypothesis R a PID made explicit and nonzero order, both of which the book's
    note supplies. The proof was checked: Bézout us + vr = 1 gives x = s(ux) for
    all x because rx = 0, and the same identity kills any element annihilated by
    s; for (b) the maps t ↦ tsa and t ↦ tka have kernels (k) and (s) by
    cancellation of the nonzero elements s and k in the domain R, and surjectivity
    of the second uses st ∈ (r) to write t = uk. Complete; no defect.
---

::: {.problem}
Let $R$ be a PID and let $A$ be a cyclic $R$-module of nonzero order $r\in R$.

(a) Show that if $s$ is relatively prime to $r$, then $sA = A$ and $A[s] = 0$.

(b) Show that if $s$ divides $r$, so $sk = r$, then $sA \cong R/(k)$ and $A[s] \cong R/(s)$.
:::

::: {.solution}
Choose a generator $a\in A$ with annihilator
$$
\operatorname{Ann}_R(a)=(r).
$$
Thus $A\cong R/(r)$ and $ra=0$.

::: pf

::: {.pf-step #s1}

If $(s,r)=1$, then $sA=A$.

::: pf-proof

By Bézout's identity there are $u,v\in R$ such that
$$
us+vr=1.
$$
For any $x\in A$, one has $rx=0$ because $A=Ra$ and $ra=0$. Hence
$$
x=(us+vr)x=s(ux)+v(rx)=s(ux)\in sA.
$$
Thus $A\subseteq sA$, while $sA\subseteq A$ is immediate. Therefore $sA=A$.

:::

:::

::: pf-step

If $(s,r)=1$, then $A[s]=0$.

::: pf-proof

Let $x\in A[s]$, so $sx=0$. With $u,v$ as in step [](#s1){.pf-ref},
$$
x=(us+vr)x=u(sx)+v(rx)=0.
$$
Thus the only element annihilated by $s$ is $0$.

:::

:::

::: pf-step

There is an isomorphism
$$
sA\cong R/(k).
$$

::: pf-proof

Suppose $s\mid r$, say $r=sk$; since $r\ne0$, also $s,k\ne0$. Define
$$
\phi:R\longrightarrow sA,
\qquad
t\longmapsto tsa.
$$
Every element of $sA$ has the form $s(xa)=xsa$, so $\phi$ is surjective.
Moreover,
$$
t\in\ker\phi
\iff tsa=0
\iff ts\in(r)=(sk).
$$
Thus $ts=usk$ for some $u\in R$. Since $R$ is a domain and $s\ne0$, cancellation
gives $t=uk$, so $t\in(k)$. Conversely, if $t=uk$, then $tsa=u(sk)a=ura=0$, so
$t\in\ker\phi$. Hence $\ker\phi=(k)$, and the first isomorphism theorem gives
$$
sA\cong R/(k).
$$

:::

:::

::: pf-step

There is an isomorphism
$$
A[s]\cong R/(s).
$$

::: pf-proof

Define
$$
\psi:R\longrightarrow A[s],
\qquad
t\longmapsto tka.
$$
The image lies in $A[s]$ because
$$
s(tka)=t(sk)a=tra=0.
$$

To prove surjectivity, let $x=ta\in A[s]$. Then $sta=0$, so
$$
st\in(r)=(sk).
$$
Hence $st=usk$ for some $u\in R$, and cancellation of the nonzero element $s$
gives $t=uk$. Thus $x=uka=\psi(u)$.

Finally,
$$
t\in\ker\psi
\iff tka=0
\iff tk\in(sk).
$$
Since $k\ne0$, cancellation gives $t\in(s)$. Conversely $(s)\subseteq\ker\psi$.
Therefore $\ker\psi=(s)$, and the first isomorphism theorem yields
$$
A[s]\cong R/(s).
$$

:::

:::

:::

:::

::: {.remark title="Variations"}
Part (b) holds over any commutative domain $R$: if $A=Ra$ with $\Ann_R(a)=(r)$ and $r=sk$ with $s,k\neq 0$, then $sA\cong R/(k)$ and $A[s]\cong R/(s)$.
:::
