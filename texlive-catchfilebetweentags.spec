Name:		texlive-catchfilebetweentags
Version:	21476
Release:	2
Summary:	Catch text delimited by docstrip tags
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/catchfilebetweentags
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfilebetweentags.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfilebetweentags.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfilebetweentags.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package (built using the facilities of catchfile) provides
a macro \catchfilebetweentags acts like the original \catchfile
but only extracts a portion of the file instead of the complete
file. The extracted portion can be delimited by strings or by
docstrip tags: %<*tag> .... %</tag> (comments in the caught
region may be included or dropped).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/catchfilebetweentags/catchfilebetweentags.sty
%doc %{_texmfdistdir}/doc/latex/catchfilebetweentags/README
%doc %{_texmfdistdir}/doc/latex/catchfilebetweentags/catchfilebetweentags.pdf
#- source
%doc %{_texmfdistdir}/source/latex/catchfilebetweentags/catchfilebetweentags.drv
%doc %{_texmfdistdir}/source/latex/catchfilebetweentags/catchfilebetweentags.dtx
%doc %{_texmfdistdir}/source/latex/catchfilebetweentags/catchfilebetweentags.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
