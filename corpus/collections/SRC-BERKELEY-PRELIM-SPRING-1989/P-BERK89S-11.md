---
schema: qual/card@1
id: P-BERK89S-11
kind: problem
title: Uniqueness of inner inverses forces a ring to be a division ring
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used uniqueness of inner inverses to make every nonzero idempotent a
    two-sided identity, then applied this to $ab$ and $ba$ for the unique
    inner inverse $b$ of each nonzero $a$.
---

::: {.problem}
Let $R$ be a ring with at least two elements. Suppose that for every nonzero $a\in R$ there is a unique $b\in R$ such that
\[
aba=a.
\]
Show that $R$ is a division ring.
:::

::: {.solution}
<1>1. If $a\neq0$ and $b$ is the unique element satisfying $aba=a$, then
$b\neq0$ and
$$
bab=b.
$$

::: {.proof}
If $b=0$, then $aba=0$, contrary to $a\neq0$. Thus $b\neq0$.

Moreover,
$$
a(bab)a=ababa=(aba)ba=aba=a.
$$
Hence $bab$ is another element $c$ satisfying $aca=a$. By uniqueness of
$b$, one has $bab=b$.
:::

<1>2. If $a\neq0$ and $b$ is as in step <1>1, then $ab$ and $ba$ are
nonzero idempotents.

::: {.proof}
Using step <1>1,
$$
(ab)^2=a(bab)=ab,
$$
and using $aba=a$,
$$
(ba)^2=b(aba)=ba.
$$
If $ab=0$, then $aba=0$, contradicting $a\neq0$. Similarly, if $ba=0$,
then $aba=a(ba)=0$, again a contradiction. Thus both idempotents are nonzero.
:::

<1>3. Every nonzero idempotent $e\in R$ is a two-sided identity for $R$.

::: {.proof}
Since $e\neq0$, the hypothesis says that there is a unique $x\in R$ with
$$
exe=e.
$$
Because $e^3=e$, the element $e$ itself has this property, so uniqueness gives
$x=e$.

Now suppose $y\in R$ satisfies $eye=0$. Then
$$
e(e+y)e=e^3+eye=e,
$$
so uniqueness again implies $e+y=e$, hence $y=0$.

Let $r\in R$. Since $e^2=e$,
$$
e(r-er)e=ere-eere=0.
$$
The preceding paragraph gives $r-er=0$, so $er=r$. Likewise,
$$
e(r-re)e=ere-eree=0,
$$
and hence $r-re=0$, so $re=r$. Therefore $e$ is a two-sided identity for
every element of $R$.
:::

<1>4. Every nonzero $a\in R$ has a two-sided inverse.

::: {.proof}
Fix $a\neq0$ and let $b$ be its unique inner inverse. By step <1>2, both
$ab$ and $ba$ are nonzero idempotents. Step <1>3 therefore says that each is
a two-sided identity for $R$. A ring has at most one two-sided identity, so
$$
ab=ba=1_R.
$$
Thus $b$ is a two-sided inverse of $a$.
:::

<1>5. The ring $R$ is a division ring.

::: {.proof}
Because $R$ has at least two elements, it has a nonzero element. Applying
steps <1>2 and <1>3 to that element produces a two-sided identity $1_R$.
By step <1>4, every nonzero element of $R$ is invertible with respect to this
identity. Hence $R$ is a division ring.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
