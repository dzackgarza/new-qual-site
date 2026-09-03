---
order: 29
title: "Real Analysis Qual Prep Week 2: Measure Theory, Fubini Tonelli"
---

# Real Analysis Qual Prep Week 2: Measure Theory, Fubini Tonelli

References:

- [@Fol13, chap. 1]

- [@SS05, chaps. 1-2]

## Convergence reminders

- **Metrics and norms** turn equality and convergence questions into estimates.

  - ![](_attachments/Pasted image 20210528184220.png)

  - To prove equality in a metric setting, it is often enough to prove the distance is zero.
    The triangle inequality is the basic tool for splitting estimates.

- **Uniform convergence**:

  - ![](_attachments/Pasted image 20210528182641.png)

  - Negating uniform convergence means finding $\eps>0$ such that for every $N$ there are $n\geq N$ and a point $x$ with $\abs{f_n(x)-f(x)}\geq\eps$; the bad point may depend on $n$.

  - For a series of functions $\sum_{k\geq1}a_k(x)$, define the partial sums $f_n(x):=\sum_{k\leq n}a_k(x)$ and apply the usual uniform-convergence criteria to $f_n$.

  - It's sometimes useful to trade the $\forall x$ in the definition with $\sup_{x\in X} \abs{f_n(x) - f(x)} < \eps$ instead.

- Compare and contrast to **pointwise convergence**, which is strictly weaker:

  - ![](_attachments/Pasted image 20210528182925.png)

  - In pointwise convergence, the threshold $N$ may depend on both $x$ and $\eps$; in uniform convergence, $N$ may depend on $\eps$ but must work for every $x$ simultaneously.

  - Note uniform implies pointwise but not conversely.

- The sup norm: $\norm{f}_\infty := \sup_{x\in X} \abs{f(x)}$.

  - A useful way to force uniform convergence: bound your sequence uniformly by a sequence that goes to zero:

  - ![](_attachments/Pasted image 20210528183356.png)

- **Sups and infs**: sup is the least upper bound, inf is the greatest lower bound.

- The $p-$test:
$$
\sum_{n\geq 1} {1 \over n^p} < \infty \iff p>1
$$

- Useful fact: convergent sums have **small tails**, i.e.
$$
\sum_{n\geq 1} a_n < \infty \implies \lim_{N\to\infty}\sum_{n\geq N} a_n = 0
$$

- Thus a tail estimate for a convergent numerical series is a standard way to prove uniform convergence.

- If you can't bound by a tail: as long as you have control over the coefficients, you can pick them to make the sum to converge "fast enough".

  - Example: for a fixed $\eps$, choose $a_n = 1/2^n$.
    Note that $\sum_{n\geq 1} 1/2^n = 1$, so choose $a_n := \eps/2^n$:
$$
\sum_{n\geq 1} a_n := \sum_{n\geq 1} {\eps \over 2^n} = \eps.
$$

- The $\eps/3$ trick:

  - ![](_attachments/Pasted image 20210528183619.png)

- **The $M\dash$test**:

  - ![](_attachments/Pasted image 20210528183827.png)

## Measure Theory

- $F_\sigma$ sets are countable unions of closed sets; the $F$ recalls French *fermé* (closed), and $\sigma$ indicates a countable union.

- $G_\delta$ sets: intersections of open sets

- $\sigma$ algebras: closed under complements, countable intersections, countable unions

- Some of the most useful properties of measures:

![](_attachments/Pasted image 20210528184432.png)

![](_attachments/Pasted image 20210528184444.png)

![](_attachments/Pasted image 20210528184451.png)

- The proof of continuity of measure contains a very useful trick: replace a sequence of sets $\ts{E_k}$ with a sequence of *disjoint* sets that either union or intersect to the same thing.

  - Example: if $A_1 \subseteq A_2 \subseteq \cdots$, set $F_1=A_1$ and $F_k = A_k \sm A_{k-1}$ for $k\geq 2$.
    Then $\Union_{k\geq 1} A_k = \Disjoint_{k\geq 1} F_k$.

- Occasionally you need some properties of **outer measures**:

![](_attachments/Pasted image 20210528184814.png)

![](_attachments/Pasted image 20210528184827.png)

- Outer measure for $\RR^n$: you consider all collections of cubes that cover your set, sum up their volumes, and take the infimum over all such collections:

![](_attachments/Pasted image 20210528184951.png)

- "Almost everywhere *blah*" : the set where *blah* does not happen has measure zero.

- "Infinitely many/all but finitely many" types of sets, which show up in Borel-Cantelli style problems

![](_attachments/Pasted image 20210528183952.png)

![](_attachments/Pasted image 20210528184004.png)

- Lemmas that sometimes show up on quals:

![](_attachments/Pasted image 20210528185216.png)

![](_attachments/Pasted image 20210528185223.png)

## Fubini-Tonelli

Quick statement:

![](_attachments/Pasted image 20210528185415.png)

This follows from Fubini's theorem, which requires **integrability** [@SS05].

![](_attachments/Pasted image 20210528185725.png)

![](_attachments/Pasted image 20210528185759.png)

And Tonelli, which only requires **measurability**:

![](_attachments/Pasted image 20210528185956.png)

![](_attachments/Pasted image 20210528190018.png)

A more precise statement appears in [@Fol13]:

![](_attachments/Pasted image 20210528185618.png)

![](_attachments/Pasted image 20210528185433.png)

Some things that qual questions are commonly based on:

![](_attachments/Pasted image 20210528190107.png)

![](_attachments/Pasted image 20210528190142.png)

![](_attachments/Pasted image 20210528190207.png)

## Qual Problems

> Suggested by Peter Woolfitt!

[[P-8RA35]]

[[P-OPH7A]]

[[P-4NYI7]]

[[P-ZCE6E]]
