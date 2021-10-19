#!/usr/bin/perl
use strict;
use 5.010001;

sub solveRuleOne
{
	my $state = "I";
	my %transitions = ("Iwu" => "S", "Sp" => "F", "Swu" => "S", "Swl" => "S", "Sc" => "S", "Ss" => "S");
	$state = $transitions{$state . &getSymbolType($_)} for(split '', $_[0]);
	return $state;
}

sub solveRuleTwo
{
	my $state = "IF";
	my %transitions = ("IFwu" => "F", "IFwl" => "F", "IFp" => "IF", "IFs" => "IF",
	"Fc" => "C", "Fwu" => "F", "Fwl" => "F", "Fp" => "IF", "Fs" => "IF",
	"Cs" => "S", "Swu" => "F", "Swl" => "F");
	$state = $transitions{$state . &getSymbolType($_)} for(split '', $_[0]);
	return $state;
}

sub solveRuleThree
{
	my $state = "IF";
	my %transitions = ("IFwu" => "IF", "IFwl" => "IF", "IFp" => "IF", "IFs" => "F", "IFc" => "IF",
	"Fwu" => "IF", "Fwl" => "IF", "Fp" => "IF", "Fc" => "IF");
	$state = $transitions{$state . &getSymbolType($_)} for(split '', $_[0]);
	return $state;
}

sub getSymbolType {
	return "wu" if $_[0] =~ m/[A-Z]/;
	return "wl" if $_[0] =~ m/[a-z]/;
	return "p" if $_[0] =~ m/\./;
	return "c" if $_[0] =~ m/,/;
	return "s" if $_[0] =~ m/\s/;
	say "Invalid character ${_[0]}";
	return "";
}

my @lines;
my $lineNum = 1;
while(<>)
{
	chomp;
	push @lines,$lineNum unless (&solveRuleOne($_) =~ m/F/ && &solveRuleTwo($_) =~ m/F/ && &solveRuleThree($_) =~ m/F/);
	$lineNum++;
}
say (@lines == 0 ? "No Problems" : join ' ',@lines);
