module Jekyll
  class TagPage < Page
    def initialize(site, base, dir, tag)

      @site = site
      @base = base
      @dir = dir.downcase.gsub(" ","-")
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag_index.html')
      self.data['tag'] = tag
      self.data['title'] = tag
    end
  end

  class TagPageGenerator < Generator
    safe true
    def generate(site)
      if site.layouts.key? 'tag_index'
        dir = site.config['tag_dir'] || 'tag'
        site.tags.keys.each do |tag|
          site.pages << TagPage.new(site, site.source, File.join(dir, tag), tag)
        end
      end
    end
  end
end
