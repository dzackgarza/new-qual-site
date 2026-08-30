---
order: 10
---

# Definitions

## Convergence and Continuity

[[D-HOKQD]]

[[D-HHVPT]]

[[FD-ST7TD]]

:::{.remark}
The main difference is that $\delta$ may depend on $x_0$ and $\eps$ in continuity, but only depends on $\eps$ in the uniform version.
I.e. once $\delta$ is fixed, for continuity one may only range over $x$, but in uniform continuity one can range over all pairs $x,y$.

:::

[[D-TVKFM]]

[[FD-5I73B]] [[FF-7JOOD]]

[[D-IYDZU]]

[[D-YZC3C]]

[[FD-ZTRHG]] [[FD-F3UU4]]

## Function Spaces

[[D-G5N6I]]

[[FD-WN55Z]] [[FF-HORGP]]

:::{.fact}
If $X$ is complete, then absolutely convergent implies convergent.

:::

[[FD-BA2WU]] [[FF-NRCZN]]

[[FD-Q7EEG]]

[[D-2MJRE]]

[[FD-SMWLB]] [[FF-HRUA3]]

[[FF-YXTQY]]

[[D-5NODS]]

[[FD-QEQIY]] [[FF-SZR6O]]

[[FD-JGBSF]] [[FF-QLQYF]]

[[D-VFNTY]]

[[FD-WHWSQ]] [[FF-VON2D]]

## Measure Theory

[[D-PAEDW]]

[[FD-AI6XN]] [[FF-JBCFQ]]

:::{.remark}
How to derive these definitions: use that $\inf$ corresponds to intersections/existence and $\sup$ corresponds to unions/forall.

- For $\liminf E_n$: 
  - $x\in \liminf E_n \iff$ there exists some $N$ such that $x\in \intersect_{n\geq N} E_n$, i.e. $x\in E_n$ for all $n\geq N$.
    So $x$ is in *all* but finitely many $n$.
  - How to remember:  $\liminf_{n} x_n = \sup_{n} \inf_{k\geq n} x_n$ for sequences, where sups look like unions and infs look like intersections.
  - Alternatively: there exists an $n$ (union) such that for all $k\geq n$ (intersection)...
    

- For $\limsup E_n$: 
  - $x\in \limsup E_n \iff$ for every $N$, there exists some $n\geq N$ such that $x\in E_n$.
    So $x$ is an infinitely many $E_n$.
  - How to remember:  $\limsup_{n} x_n = \inf{n} \sup{k\geq n} x_n$ for sequences, where sups look like unions and infs look like intersections.
  - Alternatively: for all $n$ (intersection) there exists a $k\geq n$ (union)...

It's also useful to note that $\liminf E_n \subseteq \limsup E_n$, since $\liminf E_n$ are elements that are eventually in all sets, and $\limsup E_n$ are elements in infinitely many sets.

Why these are useful: for finite measure spaces,
\[
\mu\qty{\liminf_n E_n }\leq \liminf_n \mu(E_n) \leq \lim_n \mu(E_n) \leq \limsup_n \mu(E_n) \leq \mu\qty{\limsup_n E_n}
.\]
If the $\limsup$ and $\liminf$ sets are equal, then one can define the set $\lim_n E_n \da \union_n E_n$ if $E_n \increasesto E$ or $\lim_n E_n \da \intersect_n E_n$ if $E_n\decreasesto E$ in which case continuity of measure states
\[
\mu\qty{\lim_n E_n} = \lim_n \mu(E_n)
.\]

:::

[[D-RPOGQ]]

[[FD-BBR6Q]] [[FD-HGESN]]

[[FD-V5ISD]]

[[D-3XE77]]

[[FD-QA5ME]] [[FD-KNEDG]]

[[D-MDJII]]

[[FD-D4S7E]] [[FT-KXFMK]]

[[FF-MXNIV]]

[[FD-6HUIM]]

[[FD-5T3HX]] [[FF-NOX4C]]

[[FD-T7SN6]]

[[FD-D7HOH]]

[[D-BF5L2]]

## Integrals and $L^p$ Spaces

[[D-R5DL3]]

[[D-3PVRB]]

[[FD-J5AFR]]

[[D-MFDEJ]]

[[D-TS42Y]]

[[FF-4WIMZ]]

[[D-5LZQ4]]

[[D-EWXAT]]

[[D-MAGRK]]

[[D-ARQFC]]

## Functional Analysis

[[D-T4LOC]]

[[D-4IXAO]]

[[D-AQX7W]]

[[D-SLYE5]]

[[D-PQIQO]]

[[D-EPSKF]]

[[D-BG455]]

[[D-7QQUO]]

