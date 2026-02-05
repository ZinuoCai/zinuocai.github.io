# ZinuoCai

## Install

```bash
# mkdocs
pip install mkdocs

# theme
pip install mkdocs-bootswatch
```

## Update

Change the footer.

Update the `base.html` of `mkdocs`. Path: `XXX/conda/envs/mkdocs/Lib/site-packages/mkdocs/themes/mkdocs/base.html`

```html
<footer class="col-md-12">
    {%- block footer %}
    <hr>
    {%- if config.copyright %}
    <p>{{ config.copyright }}</p>
    {%- endif %}
    
    <!-- 添加上次更新时间 -->
    {%- if build_date_utc %}
    <script>
    // 在客户端转换时区并显示
    document.addEventListener('DOMContentLoaded', function() {
        const utcDate = '{{ build_date_utc }}';
        if (utcDate) {
            const date = new Date(utcDate);
            const options = {
                year: 'numeric',
                month: '2-digit',
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                timeZoneName: 'short'
            };
            const formattedDate = date.toLocaleString('zh-CN', options);
            
            // 找到更新时间元素并设置内容
            const updateElement = document.querySelector('.last-updated');
            if (updateElement) {
                updateElement.textContent = 'Last updated: ' + formattedDate;
            }
        }
    });
    </script>
    <p class="last-updated">{% trans date=build_date_utc %}Last updated: {{ date }} UTC{% endtrans %}</p>
    {%- endif %}
    
    <p>{% trans mkdocs_link='<a href="https://www.mkdocs.org/">MkDocs</a>' %}Documentation built with {{ mkdocs_link }}.{% endtrans %}</p>
    {%- endblock %}
</footer>
```

## Depoly

```bash
mkdocs gh-deploy
```