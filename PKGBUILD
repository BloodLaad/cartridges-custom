pkgname=cartridges-custom
pkgver=2.7.2.custom1
pkgrel=1
pkgdesc="A GTK4 + Libadwaita game launcher with custom scrapers"
arch=(any)
url="https://github.com/BloodLaad/cartridges-custom"
license=(GPL3)
depends=(gtk4 libadwaita gdk-pixbuf2 gobject-introspection-runtime python python-gobject python-requests python-yaml
         python-pillow python-urllib3 dconf hicolor-icon-theme)
makedepends=(blueprint-compiler meson)
checkdepends=(appstream-glib)
optdepends=("steam: Valve's digital software delivery system"
            'heroic-games-launcher: Native GOG and Epic Games launcher for Linux'
            'bottles: Easily manage wine and proton prefix')
#source=(${pkgname}-${pkgver}.tar.gz::$url/archive/v${pkgver}.tar.gz)
#b2sums=('462c4117e0cc3050b9deac508704e863dab0f389e825007392a51a44fffb9eb9a98d8f915379b1eb7ecb696ed85a9027a3705835038109d814e96282a865883f')

build() {
  arch-meson build  -D tiff_compression=jpeg
  meson compile -C build
}

check() {
  # https://github.com/kra-mo/cartridges/issues/206
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --destdir "$pkgdir"
}