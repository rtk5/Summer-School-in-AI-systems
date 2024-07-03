; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"print"(i32 %".1")

define i32 @"fib"(i32 %"n")
{
alloca-odepwntb:
  %"n.1" = alloca i32
  %"g" = alloca i32
  %"h" = alloca i1
  %"a" = alloca i32
  %"b" = alloca i32
  %"v1" = alloca i32
  %"v2" = alloca i32
  %"v3" = alloca i32
  %"v4" = alloca i32
  %"res" = alloca i32
  br label %"entry-aamnilhh"
entry-aamnilhh:
  store i32 %"n", i32* %"n.1"
  store i32 2, i32* %"g"
  %".5" = load i32, i32* %"n.1"
  %".6" = load i32, i32* %"g"
  %"h.1" = icmp slt i32 %".5", %".6"
  store i1 %"h.1", i1* %"h"
  %".8" = load i1, i1* %"h"
  br i1 %".8", label %"lb", label %"lr"
lb:
  %".10" = load i32, i32* %"n.1"
  ret i32 %".10"
lr:
  store i32 1, i32* %"a"
  store i32 2, i32* %"b"
  %".14" = load i32, i32* %"n.1"
  %".15" = load i32, i32* %"a"
  %"v1.1" = sub i32 %".14", %".15"
  store i32 %"v1.1", i32* %"v1"
  %".17" = load i32, i32* %"n.1"
  %".18" = load i32, i32* %"b"
  %"v2.1" = sub i32 %".17", %".18"
  store i32 %"v2.1", i32* %"v2"
  %".20" = load i32, i32* %"v1"
  %"v3.1" = call i32 @"fib"(i32 %".20")
  store i32 %"v3.1", i32* %"v3"
  %".22" = load i32, i32* %"v2"
  %"v4.1" = call i32 @"fib"(i32 %".22")
  store i32 %"v4.1", i32* %"v4"
  %".24" = load i32, i32* %"v3"
  %".25" = load i32, i32* %"v4"
  %"res.1" = add i32 %".24", %".25"
  store i32 %"res.1", i32* %"res"
  %".27" = load i32, i32* %"res"
  ret i32 %".27"
}

define void @"main"()
{
alloca-trwsdmtt:
  %"n" = alloca i32
  %"d" = alloca i32
  %"tmp" = alloca i32
  br label %"entry-pieaalwn"
entry-pieaalwn:
  store i32 7, i32* %"n"
  %".3" = load i32, i32* %"n"
  %"d.1" = call i32 @"fib"(i32 %".3")
  store i32 %"d.1", i32* %"d"
  %".5" = load i32, i32* %"d"
  %"tmp.1" = call i32 @"print"(i32 %".5")
  store i32 %"tmp.1", i32* %"tmp"
  ret void
}

