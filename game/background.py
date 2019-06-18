import pytmx
from etc.setup import Setup


class Fence:
    def __init__(self, tmx):
        self.gameMap = pytmx.load_pygame(Setup.maps + tmx, pixelalpha=True)
        self.mapwidth = self.gameMap.tilewidth * self.gameMap.width
        self.mapheight = self.gameMap.tileheight * self.gameMap.height

    def render(self, surface, start=0, limit=65535):
        c = -1
        for layer in self.gameMap.visible_layers:
            c += 1
            if c < start:
                continue
            if c > limit:
                return
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.gameMap.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))