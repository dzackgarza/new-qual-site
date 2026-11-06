# Exact certificates for the finite computations of the Chapter 8 direct-product
# cards (SRC-CH8-DIRECT-PRODUCT-SOLUTION-OUTLINES, Gallian, Contemporary Abstract
# Algebra, 7th edition, Chapter 8, printed pages 167-170).
#
# What this file is.  Each block below is one card of the collection, and each
# `chk` line is one numbered assertion about a particular finite group: a count
# of subgroups, a count of elements of a given order, an isomorphism test, or a
# decomposition.  The groups are GAP's own objects (`AbelianGroup`,
# `CyclicGroup`, `DirectProduct`, `Units(ZmodnZ(n))`, `AutomorphismGroup`), the
# subgroup and element data come from GAP's library, and nothing here recomputes
# a group by hand.  A failing assertion prints FAIL and the script exits non-zero,
# so a green run is evidence for exactly the assertions it contains.
#
# What this file is not.  It is a finite set of checks of the particular groups
# the cards display.  It is not a proof of any uniform statement: the general
# statements of the same collection (the finitary direct product is a group,
# G x {e} is normal with quotient H, the product is abelian iff the factors are,
# the order of a tuple in a finite product) are proved in
# proofs/cards/CH8DirectProduct.lean, which is the certificate for those cards.
#
# Run:  gap -q proofs/cards/CH8DirectProduct.g
#
# Status of the recorded run: PASSED, 56 checks, 0 failures ("ALL CHECKS PASSED",
# exit 0).
#
#   GAP 4.14.0 at /opt/math/bin/gap on the VM this repository was checked out in
#   (x86_64 Linux).  The run is recorded with that interpreter; the assertions
#   are library facts about the named groups, so any GAP with the `zmodnz`
#   package reproduces them.  A GAP error aborts the read of this file without
#   reaching the verdict line, so a green run is one that prints the line
#   "ALL CHECKS PASSED" with the count above.

fails := 0;;
checks := 0;;
chk := function(name, cond)
  if cond = true then
    checks := checks + 1;
    Print("PASS  ", name, "\n");
  else
    Print("FAIL  ", name, "\n");
    fails := fails + 1;
  fi;
end;;

# ---------------------------------------------------------------- P-CH8-2
# Z_2 + Z_2 + Z_2 has exactly seven subgroups of order 2.
p2 := AbelianGroup([2,2,2]);;
chk("P-CH8-2 exactly seven subgroups of order 2 in Z2+Z2+Z2",
    Length(Filtered(AllSubgroups(p2), s -> Size(s) = 2)) = 7);

# ---------------------------------------------------------------- P-CH8-6
# Z_8 + Z_2 and Z_4 + Z_4 are separated by element orders.
a6 := AbelianGroup([8,2]);;
b6 := AbelianGroup([4,4]);;
oa := Collected(List(a6, Order));;
ob := Collected(List(b6, Order));;
Print("  Z8+Z2 element orders: ", oa, "\n");
Print("  Z4+Z4 element orders: ", ob, "\n");
chk("P-CH8-6 Z8+Z2 has an element of order 8 and Z4+Z4 does not",
    Maximum(List(oa, x -> x[1])) = 8 and Maximum(List(ob, x -> x[1])) = 4);
chk("P-CH8-6 the element-order multisets differ, so the groups are not isomorphic", oa <> ob);
chk("P-CH8-6 four elements of order 4 in Z8+Z2 and twelve in Z4+Z4",
    Number(List(a6), g -> Order(g) = 4) = 4 and Number(List(b6), g -> Order(g) = 4) = 12);

# ---------------------------------------------------------------- P-CH8-10
# Z_3 + Z_9 has eighteen elements of order 9.
t10 := AbelianGroup([3,9]);;
chk("P-CH8-10 exactly 18 elements of order 9 in Z3+Z9",
    Number(List(t10), g -> Order(g) = 9) = 18);

# ---------------------------------------------------------------- P-CH8-13
# For each n = 2..6 the groups Z_{n^2} and Z_n + Z_n have order n^2 and are not
# isomorphic, the maximum element order being the invariant that separates them.
for n13 in [2..6] do
  c13 := CyclicGroup(n13^2);;
  s13 := AbelianGroup([n13,n13]);;
  chk(Concatenation("P-CH8-13 n=", String(n13),
      ": order n^2 both, max element order ", String(Maximum(List(c13, Order))),
      " against ", String(Maximum(List(s13, Order)))),
      Size(c13) = n13^2 and Size(s13) = n13^2
      and Maximum(List(c13, Order)) = n13^2 and Maximum(List(s13, Order)) = n13
      and AbelianInvariants(c13) <> AbelianInvariants(s13));
od;

# ---------------------------------------------------------------- P-CH8-14
# D_n is not isomorphic to Z_n + Z_2: the first is nonabelian, the second abelian.
for n14 in [3..10] do
  chk(Concatenation("P-CH8-14 D_", String(n14),
      " is nonabelian while Z_n+Z_2 is abelian"),
      not IsAbelian(DihedralGroup(IsPermGroup, 2*n14))
      and IsAbelian(AbelianGroup([n14,2])));
od;

# ---------------------------------------------------------------- P-CH8-19
# For divisors r | m and s | n, the subgroup <(m/r, 0), (0, n/s)> of Z_m + Z_n has
# order r s and abelian type Z_r + Z_s.
bad19 := 0;;
for m19 in [1..12] do
  for n19 in [1..12] do
    for r19 in DivisorsInt(m19) do
      for s19 in DivisorsInt(n19) do
        g19 := AbelianGroup([m19,n19]);;
        k19 := Subgroup(g19, [g19.1^(m19/r19), g19.2^(n19/s19)]);;
        if not (Size(k19) = r19*s19
                and AbelianInvariants(k19) = AbelianInvariants(AbelianGroup([r19,s19]))) then
          bad19 := bad19 + 1;
          Print("  counterexample: m=", m19, " n=", n19, " r=", r19, " s=", s19, "\n");
        fi;
      od;
    od;
  od;
od;
chk("P-CH8-19 for all m,n <= 12 and all divisors r|m, s|n the subgroup is Z_r+Z_s", bad19 = 0);

# ---------------------------------------------------------------- P-CH8-20
# Z_12 + Z_18 has a subgroup isomorphic to Z_9 + Z_4.
g20 := AbelianGroup([12,18]);;
k20 := Subgroup(g20, [g20.1^3, g20.2^2]);;
chk("P-CH8-20 <(3,0),(0,2)> has order 36 and type Z4+Z9",
    Size(k20) = 36 and AbelianInvariants(k20) = [4,9]);

# ---------------------------------------------------------------- P-CH8-23
# Every nonidentity element of Z_3 + Z_3 + Z_3 has order 3, and the same holds for
# Z_3^n, n = 1..4.
t23 := AbelianGroup([3,3,3]);;
chk("P-CH8-23 all 26 nonidentity elements of Z3^3 have order 3",
    Number(List(t23), g -> Order(g) = 3) = 26);
chk("P-CH8-23 every nonidentity element of Z3^n has order 3, n = 1..4",
    ForAll([1..4], n -> Number(List(AbelianGroup(List([1..n], i -> 3)),
                                   g -> Order(g) = 3), x -> x) = 3^n - 1));;

# ---------------------------------------------------------------- P-CH8-26
# S_3 + Z_2 is D_6 and is not Z_12, Z_6 + Z_2 or A_4.
g26 := DirectProduct(SymmetricGroup(3), CyclicGroup(2));;
chk("P-CH8-26 S3+Z2 has order 12", Size(g26) = 12);
chk("P-CH8-26 S3+Z2 is isomorphic to D6 of order 12",
    IsomorphismGroups(g26, DihedralGroup(IsPermGroup,12)) <> fail);
chk("P-CH8-26 S3+Z2 is not cyclic, so not Z12", not IsCyclic(g26));
chk("P-CH8-26 S3+Z2 is not isomorphic to Z6+Z2",
    IsomorphismGroups(g26, AbelianGroup([6,2])) = fail);
chk("P-CH8-26 S3+Z2 is not isomorphic to A4",
    IsomorphismGroups(g26, AlternatingGroup(4)) = fail);

# ---------------------------------------------------------------- P-CH8-30
# The subgroups of order 4 of Z_4 + Z_4: seven in all, six cyclic and one
# elementary abelian.
g30 := AbelianGroup([4,4]);;
s30 := Filtered(AllSubgroups(g30), s -> Size(s) = 4);;
Print("  order-4 subgroups of Z4+Z4: ", List(s30, AbelianInvariants), "\n");
chk("P-CH8-30 Z4+Z4 has seven subgroups of order 4", Length(s30) = 7);
chk("P-CH8-30 six of them are cyclic of order 4",
    Number(s30, s -> AbelianInvariants(s) = [4]) = 6);
chk("P-CH8-30 one of them is Z2+Z2, namely {0,2} + {0,2}",
    Number(s30, s -> AbelianInvariants(s) = [2,2]) = 1
    and Size(Subgroup(g30, [g30.1^2, g30.2^2])) = 4
    and AbelianInvariants(Subgroup(g30, [g30.1^2, g30.2^2])) = [2,2]);

# ---------------------------------------------------------------- P-CH8-36
# Z_12 + Z_4 + Z_15 has a subgroup of order 9.
g36 := AbelianGroup([12,4,15]);;
chk("P-CH8-36 the 3-part of Z12+Z4+Z15 is a subgroup of order 9",
    Size(SylowSubgroup(g36, 3)) = 9);
chk("P-CH8-36 the subgroup <4> + <5> of Z12+Z15, the 3-torsion in each, has order 9",
    Size(Subgroup(g36, [g36.1^4, g36.3^5])) = 9);

# ---------------------------------------------------------------- P-CH8-38
# The matrix group H over Z_3 is abelian of order 9 and is Z_3 + Z_3, not Z_9.
z38 := Z(3)^0;;
h38 := Group([[[1,1,0],[0,1,0],[0,0,1]]*z38, [[1,0,1],[0,1,0],[0,0,1]]*z38]);;
chk("P-CH8-38 |H| = 9", Size(h38) = 9);
chk("P-CH8-38 H is abelian", IsAbelian(h38));
chk("P-CH8-38 H is Z3+Z3, not Z9", AbelianInvariants(h38) = [3,3] and not IsCyclic(h38));

# ---------------------------------------------------------------- P-CH8-49
# Aut(U(25)) is Z_4 + Z_2.
u25 := Units(ZmodnZ(25));;
chk("P-CH8-49 U(25) is cyclic of order 20", IsCyclic(u25) and Size(u25) = 20);
chk("P-CH8-49 Aut(U(25)) has order 8 and invariants [2,4], so it is Z4+Z2",
    Size(AutomorphismGroup(u25)) = 8 and AbelianInvariants(AutomorphismGroup(u25)) = [2,4]);

# ---------------------------------------------------------------- P-CH8-52, P-CH8-53
# Two isomorphism tests between direct products of cyclic groups, decided by the
# abelian invariants.
x52 := AbelianGroup([10,12,6]);;
y52 := AbelianGroup([60,6,2]);;
z53 := AbelianGroup([15,4,12]);;
Print("  invariants of Z10+Z12+Z6: ", AbelianInvariants(x52), "\n");
Print("  invariants of Z60+Z6+Z2:  ", AbelianInvariants(y52), "\n");
Print("  invariants of Z15+Z4+Z12: ", AbelianInvariants(z53), "\n");
chk("P-CH8-52 Z10+Z12+Z6 and Z60+Z6+Z2 have equal invariants, so are isomorphic",
    AbelianInvariants(x52) = AbelianInvariants(y52));
chk("P-CH8-53 Z10+Z12+Z6 and Z15+Z4+Z12 have different invariants, so are not",
    AbelianInvariants(x52) <> AbelianInvariants(z53));

# ---------------------------------------------------------------- P-CH8-55
# The isomorphisms Z_12 -> Z_4 + Z_3 are the images of a generator: four of them.
t55 := AbelianGroup([4,3]);;
chk("P-CH8-55 Z4+Z3 is cyclic of order 12", IsCyclic(t55) and Size(t55) = 12);
chk("P-CH8-55 Z4+Z3 has four generators, hence four isomorphisms from Z12",
    Number(List(t55), g -> Order(g) = 12) = 4);
chk("P-CH8-55 the generators are (1,1), (3,1), (1,2), (3,2)",
    Set(Filtered(Elements(t55), g -> Order(g) = 12)) =
    Set([t55.1^1*t55.2^1, t55.1^3*t55.2^1, t55.1^1*t55.2^2, t55.1^3*t55.2^2]));

# ---------------------------------------------------------------- P-CH8-56
# Among the isomorphisms Z_3 + Z_5 -> Z_15 exactly one takes (2,3) to 2, and its
# preimage of 1 is (1,4).
dom56 := AbelianGroup([3,5]);;
ran56 := CyclicGroup(15);;
homs56 := AllHomomorphisms(dom56, ran56);;
good56 := Filtered(Filtered(homs56, IsBijective),
                   h -> ImageElm(h, dom56.1^2 * dom56.2^3) = ran56.1^2);;
Print("  homomorphisms Z3+Z5 -> Z15: ", Length(homs56),
      ", isomorphisms: ", Length(Filtered(homs56, IsBijective)),
      ", with phi(2,3)=2: ", Length(good56), "\n");
chk("P-CH8-56 exactly one isomorphism has phi(2,3) = 2", Length(good56) = 1);
chk("P-CH8-56 its preimage of 1 is (1,4)",
    List(Filtered(Elements(dom56), x -> ImageElm(good56[1], x) = ran56.1))
    = [dom56.1^1 * dom56.2^4]);

# ---------------------------------------------------------------- P-CH8-67
# U(165) as an external direct product of U-groups, in the four ways that group
# the three primes 3, 5, 11.
u165 := Units(ZmodnZ(165));;
chk("P-CH8-67 |U(165)| = 80", Size(u165) = 80);
for pair67 in [[11,15],[3,55],[5,33]] do
  prod67 := DirectProduct(Units(ZmodnZ(pair67[1])), Units(ZmodnZ(pair67[2])));;
  chk(Concatenation("P-CH8-67 U(165) = U(", String(pair67[1]), ") + U(",
                    String(pair67[2]), ")"),
      Size(prod67) = 80 and IsomorphismGroups(u165, prod67) <> fail);
od;
prod67b := DirectProduct(DirectProduct(Units(ZmodnZ(3)), Units(ZmodnZ(5))),
                         Units(ZmodnZ(11)));;
chk("P-CH8-67 U(165) = U(3) + U(5) + U(11)",
    Size(prod67b) = 80 and IsomorphismGroups(u165, prod67b) <> fail);
chk("P-CH8-67 these are the four ways: the partitions of the three primes into at least two blocks",
    Number(PartitionsSet([3,5,11]), p -> Length(p) >= 2) = 4);;

# ---------------------------------------------------------------- P-CH8-68
# The counts in Aut(Z_20): four elements of order 4 and three of order 2.
a68 := AutomorphismGroup(CyclicGroup(20));;
chk("P-CH8-68 |Aut(Z20)| = 8 with invariants [2,4]",
    Size(a68) = 8 and AbelianInvariants(a68) = [2,4]);
chk("P-CH8-68 four elements of order 4", Number(List(a68), a -> Order(a) = 4) = 4);
chk("P-CH8-68 three elements of order 2", Number(List(a68), a -> Order(a) = 2) = 3);

# ------------------------------------------------- The cyclicity criteria
# The criterion the collection's solutions use: Z_m + Z_n is cyclic exactly when
# gcd(m,n) = 1, and with more factors exactly when the orders are pairwise
# coprime.  Both are checked over a range, and the "cyclic product has cyclic
# factors" half over all groups of order at most 8.
badc := 0;;
for mc in [2..20] do
  for nc in [2..20] do
    if IsCyclic(AbelianGroup([mc,nc])) <> (Gcd(mc,nc) = 1) then badc := badc + 1; fi;
  od;
od;
chk("Z_m+Z_n cyclic iff gcd(m,n)=1, for 2 <= m,n <= 20", badc = 0);

badc := 0;;
for ac in [2..8] do
  for bc in [2..8] do
    for cc in [2..8] do
      pw := (Gcd(ac,bc)=1) and (Gcd(ac,cc)=1) and (Gcd(bc,cc)=1);
      if IsCyclic(AbelianGroup([ac,bc,cc])) <> pw then badc := badc + 1; fi;
    od;
  od;
od;
chk("Z_a+Z_b+Z_c cyclic iff pairwise coprime, for 2 <= a,b,c <= 8", badc = 0);

badc := 0;;
for ordc in [2..8] do
  for ic in [1..NumberSmallGroups(ordc)] do
    for jc in [1..NumberSmallGroups(ordc)] do
      gc := SmallGroup(ordc,ic);;
      hc := SmallGroup(ordc,jc);;
      if IsCyclic(DirectProduct(gc,hc)) and not (IsCyclic(gc) and IsCyclic(hc)) then
        badc := badc + 1;
      fi;
    od;
  od;
od;
chk("G+H cyclic implies G and H cyclic, all groups of order 2..8", badc = 0);

# ------------------------------------------------------------------- verdict
Print("\n", checks, " checks passed, ", fails, " failed\n");
if fails > 0 then
  Print("SOME CHECKS FAILED\n");
  QUIT_GAP(1);
else
  Print("ALL CHECKS PASSED\n");
  QUIT_GAP(0);
fi;
