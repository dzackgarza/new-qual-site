---
schema: qual/card@1
id: E-SMI-8000E-MT4
kind: problem
title: Surjective non-injective endomorphisms and noetherian modules
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both parts with Smith 8000 Fall 2006 midterm problem 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used surjectivity of every iterate to lift a fixed nonzero kernel element and witness each strict kernel inclusion, then applied ACC."
---

::: {.exercise}
(a) If $f: M \to M$ is a surjective endomorphism of an $R$ module that is not injective, prove that $\ts{\ker(f^n)}$, $n = 1, 2, 3, \ldots$, is a strictly increasing sequence of submodules.

(b) What can you conclude about a surjective endomorphism of a noetherian module?
:::

::: solution
<1>1. The kernels of the iterates form an increasing chain.
::: proof
For every $n\ge1$, if
$$
m\in\ker(f^n),
$$
then
$$
f^{n+1}(m)=f(f^n(m))=0.
$$
Hence
$$
\ker(f^n)\subseteq\ker(f^{n+1}).
$$
:::

<1>2. Every inclusion is strict when $f$ is surjective but not injective.
::: proof
Because $f$ is not injective, choose
$$
0\ne x\in\ker f.
$$
Since $f$ is surjective, every iterate $f^n$ is surjective. Thus for each
$n\ge1$ there is $y_n\in M$ such that
$$
f^n(y_n)=x.
$$
Then
$$
f^{n+1}(y_n)=f(x)=0,
$$
so
$$
y_n\in\ker(f^{n+1}).
$$
But
$$
f^n(y_n)=x\ne0,
$$
so
$$
y_n\notin\ker(f^n).
$$
Therefore
$$
\boxed{
\ker f\subsetneq\ker(f^2)\subsetneq\ker(f^3)
\subsetneq\cdots.}
$$
:::

<1>3. A surjective endomorphism of a noetherian module is injective.
::: proof
If $M$ is noetherian, its submodules satisfy the ascending chain condition.
The strictly increasing chain in step <1>2 is therefore impossible. Hence a
surjective endomorphism
$$
f:M\to M
$$
cannot fail to be injective. Thus every surjective endomorphism of a
noetherian module is an automorphism:
$$
\boxed{f\text{ surjective and }M\text{ noetherian}
\Longrightarrow f\text{ injective}.}
$$
:::
:::
