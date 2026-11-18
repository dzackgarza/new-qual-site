---
schema: qual/card@1
id: E-MUN-4-1
kind: problem
title: Laws of algebra for $\RR$ from the field axioms
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 1, printed p. 34; the twenty
    parts (a)-(t) are stored as printed, including the hint to compute (x+0)x in (b) and
    the axiom range (1)-(5).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.1,
    printed pp. 38-44 (tmp/sources/munkres-solutions-whitman.pdf), which does all twenty
    parts from the axioms in order and cites earlier parts as it goes. His (b) uses the
    book's hint exactly as the card does: (x+0)x = x^2 + 0x while x+0 = x, so (a) gives
    0x = 0. No defect found.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The stored statement carried only parts (a)--(e) of the exercise. Read against Munkres,
    *Topology* (2000), §4 Exercise 1, printed p. 34, which prints twenty parts (a)--(t); the
    statement now carries all twenty as printed, with the printed hint retained under (b).
    No other field changed, and the retained solution already proved all twenty parts.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the twenty-part prose solution into Lamport steps, one step per printed part
    with (h) split into its two identities as sub-steps. The argument is transcribed from the
    retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual*
    (30 November 2019), Exercise 4.1, printed pp. 38--44. Each step uses only axioms (1)--(5)
    and the earlier parts, as the exercise requires; no division is used before (i).
---
::: {.exercise}
Prove the following "laws of algebra" for $\RR$, using only axioms (1)--(5):

(a) If $x+y=x$, then $y=0$.

(b) $0\cdot x=0$. [Hint: Compute $(x+0)\cdot x$.]

(c) $-0=0$.

(d) $-(-x)=x$.

(e) $x(-y)=-(xy)=(-x)y$.

(f) $(-1)x=-x$.

(g) $x(y-z)=xy-xz$.

(h) $-(x+y)=-x-y$; $\quad -(x-y)=-x+y$.

(i) If $x\neq 0$ and $x\cdot y=x$, then $y=1$.

(j) $x/x=1$ if $x\neq 0$.

(k) $x/1=x$.

(l) $x\neq 0$ and $y\neq 0$ imply $xy\neq 0$.

(m) $(1/y)(1/z)=1/(yz)$ if $y,z\neq 0$.

(n) $(x/y)(w/z)=(xw)/(yz)$ if $y,z\neq 0$.

(o) $(x/y)+(w/z)=(xz+wy)/(yz)$ if $y,z\neq 0$.

(p) $x\neq 0$ implies $1/x\neq 0$.

(q) $1/(w/z)=z/w$ if $w,z\neq 0$.

(r) $(x/y)/(w/z)=(xz)/(yw)$ if $y,w,z\neq 0$.

(s) $(ax)/y=a(x/y)$ if $y\neq 0$.

(t) $(-x)/y=x/(-y)=-(x/y)$ if $y\neq 0$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.1, printed pp. 38--44** (`tmp/sources/munkres-solutions-whitman.pdf`), which proves the twenty parts in order from axioms (1)--(5) alone, citing the earlier parts as they are established. The steps below are his argument; the statement is Munkres, *Topology* (2000), §4 Exercise 1, printed p. 34, all twenty parts as printed.

::: pf

::: {.pf-step #a}
(a) If $x+y=x$ then $y=0$.

::: pf-proof
The hypothesis and the axiom $x+0=x$ give $x+y=x+0$. Adding $-x$ on the left gives $(-x)+x+y=(-x)+x+0$, that is $0+y=0+0$, so $y=0$.
:::
:::

::: {.pf-step #b}
(b) $0\cdot x=0$.

::: pf-proof
Since $x+0=x$, multiplying by $x$ gives $(x+0)x=x\cdot x$. By distributivity the left side is $x\cdot x+0\cdot x$, so $x\cdot x+0\cdot x=x\cdot x$, and part [](#a){.pf-ref} with $x$ replaced by $x\cdot x$ gives $0\cdot x=0$.
:::
:::

::: {.pf-step #c}
(c) $-0=0$.

::: pf-proof
Both $0$ and $-0$ satisfy $0+u=0$: the first by the axiom $0+0=0$, the second by the definition of $-0$. Part [](#a){.pf-ref} applied to $0+u=0$ gives $u=0$, so $-0=0$.
:::
:::

::: {.pf-step #d}
(d) $-(-x)=x$.

::: pf-proof
$(-x)+x=0$ by the definition of $-x$ and commutativity, so $x$ satisfies $(-x)+u=0$; but so does $u=-(-x)$. The additive inverse is unique — if $u$ and $u'$ both satisfy $x+u=0=x+u'$, then $u=u'+0=u'+(x+u'')$ with $u''=u$ gives $u=u'$ by part [](#a){.pf-ref} — hence $-(-x)=x$.
:::
:::

::: {.pf-step #e}
(e) $x(-y)=-(xy)=(-x)y$.

::: pf-proof
$(-y)+y=0$, so $x((-y)+y)=x\cdot0=0$ by part [](#b){.pf-ref}, and by distributivity $x(-y)+xy=0$. Thus $x(-y)$ is an additive inverse of $xy$, and by the uniqueness used in part [](#d){.pf-ref} it equals $-(xy)$. Interchanging the roles of $x$ and $y$ in this argument with $yx=xy$ gives $y(-x)=-(yx)=-(xy)$, and by commutativity $(-x)y=y(-x)$, so $(-x)y=-(xy)$.
:::
:::

::: {.pf-step #f}
(f) $(-1)x=-x$.

::: pf-proof
Put $y=1$ in part [](#e){.pf-ref}: $(-1)x=-(1\cdot x)=-x$, using the axiom $1\cdot x=x$.
:::
:::

::: {.pf-step #g}
(g) $x(y-z)=xy-xz$.

::: pf-proof
$y-z=y+(-z)$ by definition, so $x(y-z)=x(y+(-z))=xy+x(-z)=xy+(-(xz))=xy-xz$, by distributivity and part [](#e){.pf-ref}.
:::
:::

::: {.pf-step #h}
(h) $-(x+y)=-x-y$ and $-(x-y)=-x+y$.

::: pf-proof

::: {.pf-step #h-sum}
$-(x+y)=-x-y$.

::: pf-proof
$(x+y)+((-x)+(-y))=x+((-x)+y)+(-y)=x+(-x)+y+(-y)=0+0=0$ by associativity and commutativity, so $(-x)+(-y)$ is the additive inverse of $x+y$, and uniqueness as in part [](#d){.pf-ref} gives $-(x+y)=-x-y$.
:::
:::

::: {.pf-step #h-diff}
$-(x-y)=-x+y$.

::: pf-proof
$x-y=x+(-y)$, so by step [](#h-sum){.pf-ref} applied to $x$ and $(-y)$, $-(x-y)=-x-(-y)=-x+y$, using part [](#d){.pf-ref} for $-(-y)=y$.
:::
:::

:::
:::

::: {.pf-step #i}
(i) If $x\neq0$ and $x\cdot y=x$ then $y=1$.

::: pf-proof
Axiom (5) gives $1/x$ with $x\cdot(1/x)=1$. Multiplying $xy=x$ by $1/x$ on the left gives $(1/x)(xy)=(1/x)x$, that is $((1/x)x)y=1$ by associativity, and $(1/x)x=1$, so $y=1$.
:::
:::

::: {.pf-step #j}
(j) $x/x=1$ if $x\neq0$.

::: pf-proof
By definition $x/x=x\cdot(1/x)$, which is $1$ by axiom (5).
:::
:::

::: {.pf-step #k}
(k) $x/1=x$.

::: pf-proof
$1/1=1$ because $1\cdot1=1$ and the multiplicative inverse is unique by the argument of part [](#d){.pf-ref} applied to multiplication. Hence $x/1=x\cdot(1/1)=x\cdot1=x$.
:::
:::

::: {.pf-step #l}
(l) $x\neq0$ and $y\neq0$ imply $xy\neq0$.

::: pf-proof
Suppose $xy=0$. Multiplying by $(1/x)(1/y)$, which exists by axiom (5), gives $1=((1/x)(1/y))(xy)=((1/x)x)((1/y)y)=1\cdot1=1$ on the one hand and $((1/x)(1/y))\cdot0=0$ on the other, so $1=0$, contrary to axiom (4).
:::
:::

::: {.pf-step #m}
(m) $(1/y)(1/z)=1/(yz)$ if $y,z\neq0$.

::: pf-proof
By part [](#l){.pf-ref} $yz\neq0$, so $1/(yz)$ exists. Then $(yz)\bigl((1/y)(1/z)\bigr)=((y(1/y))(z(1/z)))=1$, so $(1/y)(1/z)$ is a multiplicative inverse of $yz$, and inverses are unique; hence $(1/y)(1/z)=1/(yz)$.
:::
:::

::: {.pf-step #n}
(n) $(x/y)(w/z)=(xw)/(yz)$ if $y,z\neq0$.

::: pf-proof
$(x/y)(w/z)=(x(1/y))(w(1/z))=(xw)\bigl((1/y)(1/z)\bigr)=(xw)\bigl(1/(yz)\bigr)=(xw)/(yz)$, using commutativity and associativity of multiplication and part [](#m){.pf-ref}.
:::
:::

::: {.pf-step #o}
(o) $(x/y)+(w/z)=(xz+wy)/(yz)$ if $y,z\neq0$.

::: pf-proof
By part [](#l){.pf-ref} $yz\neq0$. Since $z/z=1$ and $y/y=1$ by part [](#j){.pf-ref}, part [](#n){.pf-ref} gives $x/y=(xz)/(yz)$ and $w/z=(wy)/(yz)$. Distributivity then gives $(xz)/(yz)+(wy)/(yz)=(xz+wy)(1/(yz))=(xz+wy)/(yz)$.
:::
:::

::: {.pf-step #p}
(p) $x\neq0$ implies $1/x\neq0$.

::: pf-proof
If $1/x=0$ then $1=x(1/x)=x\cdot0=0$ by part [](#b){.pf-ref}, contradicting axiom (4).
:::
:::

::: {.pf-step #q}
(q) $1/(w/z)=z/w$ if $w,z\neq0$.

::: pf-proof
By part [](#l){.pf-ref} $wz\neq0$, so $w/z$ is nonzero and has an inverse. Now $(w/z)(z/w)=((wz)/(zw))=1$ by part [](#n){.pf-ref}, so $z/w$ is a multiplicative inverse of $w/z$; uniqueness gives $1/(w/z)=z/w$.
:::
:::

::: {.pf-step #r}
(r) $(x/y)/(w/z)=(xz)/(yw)$ if $y,w,z\neq0$.

::: pf-proof
$(x/y)/(w/z)=(x/y)\bigl(1/(w/z)\bigr)=(x/y)(z/w)=(xz)/(yw)$ by part [](#q){.pf-ref} and part [](#n){.pf-ref}.
:::
:::

::: {.pf-step #s}
(s) $(ax)/y=a(x/y)$ if $y\neq0$.

::: pf-proof
$(ax)/y=(ax)(1/y)=a\bigl(x(1/y)\bigr)=a(x/y)$, by associativity and commutativity of multiplication.
:::
:::

::: {.pf-step #t}
(t) $(-x)/y=x/(-y)=-(x/y)$ if $y\neq0$.

::: pf-proof
$(-x)/y=(-x)(1/y)=-\bigl(x(1/y)\bigr)=-(x/y)$ by part [](#e){.pf-ref}. Also $(-y)\bigl(-(1/y)\bigr)=y(1/y)=1$ by part [](#e){.pf-ref}, so $1/(-y)=-(1/y)$ and $x/(-y)=x\bigl(-(1/y)\bigr)=-(x/y)$. Hence the three expressions agree.
:::
:::

::: {.pf-step}
All twenty laws of algebra (a)--(t) hold in $\RR$ on axioms (1)--(5) alone.

::: pf-proof
Steps [](#a){.pf-ref} through [](#t){.pf-ref} prove the twenty parts in order, each using only the field axioms and the earlier parts.
:::
:::

:::
:::
