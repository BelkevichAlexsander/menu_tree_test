from django import template
from django.shortcuts import get_object_or_404
from ..models import MenuCategories
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(MenuCategories, name=menu_name, parent=None)
    # print('menu_draw: context   >    ', context)
    # print('menu_draw: menu_name   >    ', menu_name)
    # print('menu_draw: menu   >    ', menu)
    local_context = {'menu_item': menu}
    requested_url = context['request'].path
    print('menu_draw: requested_url   >    ', requested_url)
    print('menu_draw: context["request"]   >    ', context['request'])
    try:
        active_menu_item = MenuCategories.objects.get(explicit_url=requested_url)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_item_ids = active_menu_item.get_elder_ids() + [active_menu_item.id]
        local_context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids

    print("draw: local context :  ", local_context)
    return local_context


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu_item_children(context, menu_item_id):
    # print('draw item: context', context)
    # print('draw item: menu_item_id', menu_item_id)
    menu_item = get_object_or_404(MenuCategories, pk=menu_item_id)
    # print('draw item: menu_item', menu_item)
    local_context = {'menu_item': menu_item}
    if 'unwrapped_menu_item_ids' in context:
        local_context['unwrapped_menu_item_ids'] = context['unwrapped_menu_item_ids']

    print('draw item: local_context     >   ', local_context)
    return local_context
