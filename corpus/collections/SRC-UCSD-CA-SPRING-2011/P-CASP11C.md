---
schema: qual/card@1
id: P-CASP11C
kind: problem
title: "Analytic continuation along different paths yielding different germs (Monodromy failure)"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
  - event: source-corrected
    by: claude
    date: 2026-11-18
    note: >-
      The example the solution gave first continued the logarithm from 1 to -1 and then told the
      reader to translate the endpoint notation to reach the prescribed b = 0; the exercise asks
      for paths from a = 1 to b = 0, so that is a mismatch between statement and example. The card
      now carries an explicit pair of paths with the prescribed endpoints, gamma(t) = 1 - t and
      sigma(t) = (1-t) + i sin(pi t), the germ of log(z - i/2) at 1, and the winding number that
      separates the terminal germs. The substance of the argument, and the reason the monodromy
      theorem does not apply, are unchanged.
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. Each
      step re-read: the disc D(1,1/4) avoids the puncture; both paths avoid i/2, checked on the
      arch by comparing sin(pi t) with 1/2; the continuation exists and is unique along each path
      because overlapping branches differ by a multiple of 2 pi i; and the loop sigma * gamma^{-1}
      is the boundary of the region between the arch and the segment, which contains i/2. Not
      claimed: any statement about continuation along paths in a simply connected domain, where
      the monodromy theorem does apply.
---

::: {.problem}
Let $a = 1$, $b = 0$, regarded as points in $\CC$.

(a) Give an example of an analytic function element $(h, D)$, with $a \in D$, and analytic continuations $(f_t, D_t)$, $(g_t, B_t)$ of $(h, D)$ along two different paths $\gamma$ and $\sigma$, such that $\gamma(0) = \sigma(0) = a$, $\gamma(1) = \sigma(1) = b$, but $[g_1]_b \neq [f_1]_b$.
Define the analytic continuations explicitly and explain briefly why these satisfy the definition of an analytic continuation.

(b) Explain why the Monodromy Theorem does not apply for your example in (a) to conclude that $[g_1]_b = [f_1]_b$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source. The example is stated for the prescribed endpoints $a=1$ and $b=0$.

::: pf

::: {.pf-step #example}
Take $c=i/2$, let $D=D(1,1/4)$ and let $h$ be the branch of $\log(z-c)$ on $D$ with $h(1)=\log(1-i/2)$, and let
$$
\gamma(t)=1-t,\qquad \sigma(t)=(1-t)+i\sin(\pi t),\qquad 0\le t\le1 .
$$

::: pf-proof
$D$ avoids $c$ because $\abs{1-i/2-1}=1/2>1/4$, so $\log(z-c)$ has a holomorphic branch there and $h$ is a function element with $1\in D$. Both paths run from $\gamma(0)=\sigma(0)=1$ to $\gamma(1)=\sigma(1)=0$, and neither meets $c=i/2$: on $\gamma$ the imaginary part is $0$, and on $\sigma$ the imaginary part is $\sin(\pi t)$, which differs from $1/2$ for every $t\in[0,1]$ where the real part is $0$, the equality $\sin(\pi t)=1/2$ occurring only at $t=1/6,5/6$ where the real part is $5/6$ and $1/6$.
:::

:::

::: {.pf-step #continuation}
The element $(h,D)$ continues along both paths, and the terminal germs at $0$ differ by $2\pi i$.

::: pf-proof
Cover the compact image of each path by finitely many discs avoiding $c$; on overlapping discs two branches of $\log(z-c)$ differ by a constant in $2\pi i\ZZ$, so the branch at each stage is the unique one agreeing with the previous on the overlap. Hence both continuations exist and are unique. The change in the argument of $z-c$ along a path equals minus $2\pi$ times the winding number of the path about $c$ plus the change of a continuous argument between the endpoints; the closed loop formed by $\sigma$ followed by the reverse of $\gamma$ is the boundary of the region between the arch $y=\sin\pi x$ and the segment $y=0$, which contains $c=(0,1/2)$, so that loop has winding number of modulus $1$ about $c$. Hence the argument changes along $\sigma$ differ from the change along $\gamma$ by $-2\pi$, and the terminal values of the continuations differ by $2\pi i$:
$$
\boxed{[f_{1}]_{0}\ne[g_{1}]_{0},\qquad f_{1}(0)-g_{1}(0)=2\pi i .}
$$
:::

:::

::: {.pf-step #monodromy}
The monodromy theorem does not apply.

::: pf-proof
That theorem requires the two paths to be homotopic with fixed endpoints inside a domain $\Omega$ containing both, into which the element continues. Any such $\Omega$ would have to contain the loop $\sigma*\gamma^{-1}$, and that loop has nonzero winding number about $c$; a domain containing a loop of nonzero winding about an omitted point is not simply connected, and the paths are not homotopic rel endpoints in it. So the hypothesis of the theorem fails, which is exactly why the terminal germs may differ:
$$
\boxed{\text{the concatenation winds once about }c=i/2,\text{ so the continuation domain is not simply connected}.}
$$
:::

:::

:::
:::
