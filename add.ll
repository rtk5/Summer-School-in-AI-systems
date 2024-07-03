; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"print"(i32 %".1")

define i32 @"main"()
{
alloca-mrehcsew:
  %"v0" = alloca i32
  %"v1" = alloca i32
  %"res" = alloca i32
  %"tmp" = alloca i32
  br label %"entry-ckpmttgj"
entry-ckpmttgj:
  store i32 9, i32* %"v0"
  store i32 -20, i32* %"v1"
  %".4" = load i32, i32* %"v0"
  %".5" = load i32, i32* %"v1"
  %"res.1" = add i32 %".4", %".5"
  store i32 %"res.1", i32* %"res"
  %".7" = load i32, i32* %"res"
  %"tmp.1" = call i32 @"print"(i32 %".7")
  store i32 %"tmp.1", i32* %"tmp"
  %".9" = load i32, i32* %"tmp"
  ret i32 %".9"
}

